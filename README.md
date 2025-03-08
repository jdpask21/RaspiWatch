# RaspiWatch

A desktop clock application built with Flet that displays time, temperature, humidity, and weather information. This application is designed to run on Raspberry Pi with a DHT22 temperature and humidity sensor, AM312 human sensor, CdS light sensor, and supports SwitchBot device control.

[日本語版はこちら](README_JP.md)

## Features

- Real-time clock display
- Current weather conditions in Osaka
- Temperature and humidity monitoring (requires DHT22 sensor)
- Weather updates every 6 hours
- Full-screen display support
- Light status detection using CdS photoresistor
  - Displays sun icon when light is on, moon icon when light is off
  - Provides binary light status detection (on/off)
- SwitchBot device control integration
  - Controls lights based on human presence detection and current light status
  - Human presence detection using AM312 PIR sensor
  - Automatic light control based on human presence and current light status

## Requirements

- Raspberry Pi
- Python 3.7+
- DHT22 temperature and humidity sensor
- AM312 human sensor
- CdS photoresistor (light sensor)
- GPIO pins D18, GPIO26, and analog input available on Raspberry Pi
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

3. Connect the CdS photoresistor:
   - Set up a voltage divider circuit with the CdS cell and a fixed resistor
   - Connect one end of the CdS cell to 3.3V
   - Connect the other end to both the analog input pin and through a resistor to ground
   - Follow the wiring guide in the documentation for precise setup

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

## Light Detection System

The application now uses a CdS photoresistor to detect the current light status in the room, which enables more intelligent light control:

- The application displays the current light status with icons in the upper right corner of the display:
  - Sun icon when light is detected as ON
  - Moon icon when light is detected as OFF

- This light detection is necessary because the SwitchBot API cannot reliably report the current status of some light devices.

- The CdS sensor provides binary (on/off) light detection. Future updates will include more precise light level measurement using a microcontroller on a breadboard to enable more granular control.

### Limitations

- The CdS sensor may falsely detect light as ON when significant natural light (such as direct sunlight through open curtains) enters the room, even if the actual room lights are OFF.
- For best results, position the CdS sensor where it can accurately detect artificial room lighting without interference from natural light sources.

## Future Updates

- Integration with microcontroller for more precise light level detection
- Support for multiple SwitchBot device types
- Enhanced light control algorithms based on light level, time of day, and human presence

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.