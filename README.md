# TECH-TITANS
# Smart Environmental Monitoring System

A low-cost **IoT-based environmental monitoring system** built using **ESP32**, audio sensors, and temperature sensors to monitor environmental conditions in real time. The system collects data from multiple sensing nodes and can transmit it wirelessly to a central gateway/dashboard for visualization and analysis.

## Key Features

* 🎙️ **Real-time noise monitoring** using audio sensors
* 🌡️ **Temperature monitoring** using temperature sensors
* 📡 **Wireless communication** between ESP32 nodes
* 📊 Centralized data collection and visualization
* ⚡ Low-cost and scalable architecture
* 🔍 Helps identify environmental changes and abnormal conditions


## Hardware Used

* ESP32 DevKit V1
* 2 × Audio/Noise Sensors
* 2 × Temperature Sensors
* Jumper wires
* USB cables / Power supply

## Software & Technologies

* Arduino IDE
* ESP32 Arduino Core
* C/C++
* ESP32 wireless communication
* Serial Monitor / Dashboard for data visualization

## Parameters Monitored

| Parameter | Sensor | Purpose |
| :--- | :--- | :--- |
| Noise Level and Source | Audio Sensor + Edge FFT | Detect environmental sound and classify the source using AI |
| Temperature | DHT Sensor | Monitor surrounding temperature and forecast short-term trends |
| Humidity | DHT Sensor | Track ambient moisture levels |

---

## Machine Learning and Innovation

To overcome the limitation of limited real-world sensor data during the prototyping phase, we employed a Hybrid Data Training Strategy:

1. **Public Dataset Augmentation:** We trained our initial Random Forest model on the "Dataset of Indoor Air Pollutants using Low-Cost Sensors" to learn baseline acoustic and environmental patterns.
2. **Real-World Fine-Tuning:** We developed a custom Python data-collection script to record over 7,000 real-world samples directly from our specific ESP32 hardware across various campus environments (Quiet, Traffic, Talking, Drill). 
3. **Dual-Model Architecture:** 
   - `esp32_audio_model_23feat.pkl`: Classifies live audio into three distinct categories using 23 extracted FFT and spectral features.
   - `nitk_temperature_scaler.pkl`: Predicts future temperature trends based on current temperature and humidity inputs.

This hybrid approach effectively bridges the "sim-to-real" gap, ensuring the machine learning models perform reliably on our specific, low-cost hardware configurations.

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/VaibhavPorwal07/TECH-TITANS.git
cd tech-titans
```
### 2.Install Python Dependencies
It is highly recommended to use a virtual environment to manage dependencies.
```bash
# Create and activate virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Install required packages
pip install flask flask-cors joblib numpy requests scikit-learn
```
### 3.Place the Machine Learning Models
Ensure the trained .pkl model files are located in the root directory of the project (the same folder as app.py):
esp32_audio_model_23feat.pkl
nitk_temperature_scaler.pkl
For Windows (PowerShell):
```powershell
(Get-Content app.py) -replace 'C:\\Users\\Ritesh Ashtkar\\', '' | Set-Content app.py
```
For Linux / macOS (sed):
```bash
sed -i 's|/home/.*\/||g' app.py
sed -i 's|C:\\Users\\.*\\||g' app.py
```
##How to Run the System
Step 1: Flash the ESP32 Nodes
Open the .ino file in the Arduino IDE.
Update the WIFI_SSID and WIFI_PASSWORD variables to match your local network credentials.
Upload the code to your ESP32 boards.
Note the IP addresses assigned to each ESP32 (visible in the Serial Monitor) and update the ESP32_NODES dictionary in app.py if necessary.
Step 2: Start the Backend Server
Ensure your virtual environment is activated, then execute the following command:
```bash
python app.py
```
You should see confirmation messages indicating the models are loaded and the server is running.
Step 3: Launch the Frontend Dashboard
You have two options to view the dashboard:
Option A (Direct File Access):
Double-click the index.html file in your file explorer, or drag and drop it into a modern web browser (Chrome, Edge, or Firefox).
Option B (Local HTTP Server - Recommended):
Serve the HTML file using a local HTTP server to prevent any browser CORS restrictions:
```bash
python -m http.server 8080
```
Then, open your browser and navigate to: http://localhost:8080

# Innovation

The main innovation is the use of **multiple distributed ESP32 sensing nodes** instead of depending on a single monitoring device. This allows environmental conditions to be observed at different locations and makes the system easier to scale by adding more sensor nodes.

The system can be further extended with:

* Machine-learning-based anomaly detection
* Historical data storage
* Location-based pollution/noise mapping
* Mobile/web dashboard
* Additional environmental sensors
* Automated alerts when readings cross defined thresholds

## Future Scope

This prototype can be developed into a complete **smart-city environmental monitoring network** by integrating additional air-quality sensors, cloud connectivity, GPS/location data, and AI-based prediction models.

## Project

Developed as a prototype for **Smart India Hackathon / IoT-based Environmental Monitoring**.
since we had verey less sensor data we ran 2ml models one with a public data set Dataset of Indoor Air Pollutants using Low-Cost Sensors and 1 we ran on our own data set.

> **Goal:** Build an affordable, scalable and real-time sensing system that can help monitor environmental conditions and support data-driven decision making.
> <img width="1882" height="862" alt="image" src="https://github.com/user-attachments/assets/90d5bf82-4691-494c-94d5-eefa076d0ac0" />


