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
* Breadboard
* USB cables / Power supply

## Software & Technologies

* Arduino IDE
* ESP32 Arduino Core
* C/C++
* ESP32 wireless communication
* Serial Monitor / Dashboard for data visualization

## 📈 Parameters Monitored

| Parameter       | Sensor             | Purpose                          |
| --------------- | ------------------ | -------------------------------- |
| 🔊 Noise Level  | Audio Sensor       | Detect environmental sound/noise |
| 🌡️ Temperature | Temperature Sensor | Monitor surrounding temperature  |

The sensor readings can be processed and transmitted to the gateway, where they can be displayed for monitoring and further analysis.

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

> **Goal:** Build an affordable, scalable and real-time sensing system that can help monitor environmental conditions and support data-driven decision making.
> <img width="1882" height="862" alt="image" src="https://github.com/user-attachments/assets/90d5bf82-4691-494c-94d5-eefa076d0ac0" />


