from flask import Flask, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import requests
import time
import threading

app = Flask(__name__)
CORS(app)

# ✅ LOAD THE ML MODEL
model = None
try:
    model = joblib.load("esp32_audio_model_23feat.pkl")
    print("✅ ML Model loaded successfully!")
except FileNotFoundError:
    print("⚠️ WARNING: 'esp32_audio_model_23feat.pkl' not found. AI prediction disabled.")

# 🌐 Multi-ESP32 Configuration
ESP32_NODES = {
    "N01": "http://10.53.22.188/",   # LHC D (Assuming this is the IP, update if different)
    "N02": "http://10.53.22.188/",   # Main Building
    "N03": "http://10.53.25.101/"    # Main Gate
}

# Keep track of node status
node_status = {node: {"online": False, "data": None} for node in ESP32_NODES}

def retry_esp32_connection():
    """Background thread that INFINITELY retries connecting to ESP32 nodes without crashing."""
    while True:
        for node_id, ip in ESP32_NODES.items():
            try:
                response = requests.get(ip, timeout=2)
                response.raise_for_status()
                data = response.json()
                node_status[node_id]["online"] = True
                node_status[node_id]["data"] = data
                # Only print on state change to keep console clean, or keep as is
            except Exception:
                node_status[node_id]["online"] = False
                # Silently fail and retry. DO NOT CRASH.
        time.sleep(3) # Retry every 3 seconds

# Start the background retry thread (daemon=True ensures it closes when Flask closes)
retry_thread = threading.Thread(target=retry_esp32_connection, daemon=True)
retry_thread.start()

@app.route("/api/live-data/<node_id>", methods=["GET"])
def get_live_data(node_id):
    if node_id not in ESP32_NODES:
        return jsonify({"status": "error", "message": "Unknown node"}), 404
    
    if node_status[node_id]["online"] and node_status[node_id]["data"]:
        data = node_status[node_id]["data"]
        features = {
            "temperature": float(data.get("temperature", 0.0)),
            "humidity": float(data.get("humidity", 0.0)),       # ✅ FIXED: Added Humidity here!
            "rms": float(data.get("rms", 0.0)),
            "peak": float(data.get("peak", 0.0)),
            "crest": float(data.get("crest", 0.0)),
            "spectral_centroid": float(data.get("spectral_centroid", 0.0)),
            "spectral_rolloff": float(data.get("spectral_rolloff", 0.0)),
            "spectral_flatness": float(data.get("spectral_flatness", 0.0)),
            "dominant_freq": float(data.get("dominant_freq", 0.0)),
        }
        fft_bands = data.get("fft_bands", [])
        for i in range(16):
            features[f"b{i}"] = float(fft_bands[i]) if i < len(fft_bands) else -6.0
            
        return jsonify({"status": "success", "node_id": node_id, "sensor_data": features})
    else:
        return jsonify({
            "status": "retrying",
            "message": f"Node {node_id} is currently offline. System is automatically retrying..."
        }), 202

@app.route("/api/sensor-data/<node_id>", methods=["GET"])
def get_sensor_data(node_id):
    if model is None:
        return jsonify({"status": "error", "message": "ML Model not loaded"}), 500

    if not node_status[node_id]["online"] or not node_status[node_id]["data"]:
        return jsonify({
            "status": "retrying",
            "message": f"Node {node_id} is offline. Retrying connection..."
        }), 202

    data = node_status[node_id]["data"]
    feature_order = [
        "rms", "peak", "crest", "spectral_centroid", "spectral_rolloff",
        "spectral_flatness", "dominant_freq"
    ] + [f"b{i}" for i in range(16)]
    
    try:
        prediction_input = []
        for feat in feature_order:
            if feat in data:
                prediction_input.append(float(data[feat]))
            elif feat.startswith("b") and "fft_bands" in data:
                idx = int(feat[1:])
                prediction_input.append(float(data["fft_bands"][idx]) if idx < len(data["fft_bands"]) else -6.0)
            else:
                prediction_input.append(0.0)
                
        prediction = model.predict(np.array(prediction_input).reshape(1, -1))[0]
        label_map = {0: "Background/Traffic", 1: "Talking", 2: "Drill"}
        
        return jsonify({
            "status": "success",
            "node_id": node_id,
            "audio_analysis": {
                "predicted_class_id": int(prediction),
                "predicted_label": label_map.get(int(prediction), "Unknown")
            },
            "raw_features": data
        })
    except Exception as e:
        return jsonify({"status": "error", "message": f"Prediction failed: {str(e)}"}), 500

@app.route("/api/all-nodes-status", methods=["GET"])
def get_all_nodes_status():
    return jsonify({
        node_id: {"online": status["online"], "ip": ESP32_NODES[node_id]} 
        for node_id, status in node_status.items()
    })

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 UNCRASHABLE MULTI-ESP32 FLASK SERVER STARTING")
    print("=" * 60)
    print("📡 Background thread is now INFINITELY retrying ESP32 connections.")
    print("🛡️ Server will NOT crash if nodes are offline.")
    print("🌐 Running on http://localhost:5000")
    print("=" * 60)
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)