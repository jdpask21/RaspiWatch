# RaspiWatch

A desktop clock application built with Flet that displays time, temperature, humidity, and weather information. This application is designed to run on Raspberry Pi with a DHT22 temperature and humidity sensor and supports SwitchBot device control.

[日本語版はこちら](README_JP.md)

## Features

- Real-time clock display
- Current weather conditions in Osaka
- Temperature and humidity monitoring (requires DHT22 sensor)
- Weather updates every 6 hours
- Full-screen display support
- SwitchBot device control integration
  - Currently supports light control using AM312 human sensor
  - Future updates will include support for multiple device types
  - Automatic light control based on human presence detection

## Requirements

- Raspberry Pi
- Python 3.7+
- DHT22 temperature and humidity sensor
- GPIO pin D18 available on Raspberry Pi
- AM312 human sensor
- SwitchBot account and compatible devices

## Hardware Setup

1. Connect the DHT22 sensor to your Raspberry Pi:
   - Connect the sensor's data pin to GPIO18 (Pin D18)
   - Connect VCC to 3.3V or 5V power
   - Connect GND to ground

2. Connect the AM312 human sensor:
   - Connect VCC to GPIO pin 2 (5V power)
   - Connect GND to GPIO pin 9 (Ground)
   - Connect OUT to GPIO pin 37 (GPIO26)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/RaspiWatch.git
```

2. Get your device ID (if not known):
```bash
python watch_app/src/get_device_id.py
```
This script will list all your available SwitchBot devices and their IDs.

3. Set up SwitchBot credentials:
```bash
python setup.py
```
You will be prompted to enter your SwitchBot API Token, Secret Token, and Device ID. For information on obtaining these credentials, please refer to the [SwitchBot API Documentation](https://github.com/OpenWonderLabs/SwitchBotAPI).

4. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

To start the application, run:
```bash
cd RaspiWatch
flet run watch_app
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.