# RaspiWatch

A desktop clock application built with Flet that displays time, temperature, humidity, and weather information. This application is designed to run on Raspberry Pi with a DHT22 temperature and humidity sensor.

[日本語版はこちら](README_JP.md)

## Features

- Real-time clock display
- Current weather conditions in Osaka
- Temperature and humidity monitoring (requires DHT22 sensor)
- Weather updates every 6 hours
- Full-screen display support

## Requirements

- Raspberry Pi
- Python 3.7+
- DHT22 temperature and humidity sensor
- GPIO pin D18 available on Raspberry Pi

## Hardware Setup

1. Connect the DHT22 sensor to your Raspberry Pi:
   - Connect the sensor's data pin to GPIO18 (Pin D18)
   - Connect VCC to 3.3V or 5V power
   - Connect GND to ground
   - Connect a 10K resistor between data and VCC pins

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/RaspiWatch.git
```

2. Install required packages:
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

---