##
# @file human_sensor.py
# @brief AM312 human sensor detection module for Raspberry Pi 3
# @details This module provides functionality to detect human presence using AM312 PIR sensor
#
# Copyright (c) 2025. All rights reserved.
##

import RPi.GPIO as GPIO
import time
from typing import Optional

class AM312Sensor:
    """
    AM312 PIR sensor controller class
    """
    def __init__(self, sensor_pin: int = 26):
        """
        Initialize AM312 sensor
        
        @param sensor_pin: GPIO pin number for sensor OUT (default: 26)
        """
        self.sensor_pin = sensor_pin
        self._is_initialized = False
        
    def initialize(self) -> bool:
        """
        Initialize GPIO settings for the sensor
        
        @retval True   Initialization successful
        @retval False  Initialization failed
        """
        try:
            # Set GPIO mode to BCM
            GPIO.setmode(GPIO.BCM)
            # Set sensor pin as input
            GPIO.setup(self.sensor_pin, GPIO.IN)
            self._is_initialized = True
            return True
        except Exception:
            self._is_initialized = False
            return False
            
    def cleanup(self) -> None:
        """
        Cleanup GPIO settings
        """
        if self._is_initialized:
            GPIO.cleanup()
            self._is_initialized = False
            
    def detect(self) -> int:
        """
        Detect human presence using AM312 sensor
        
        @retval  1  Human detected
        @retval  0  No human detected
        @retval -1  Error occurred
        """
        if not self._is_initialized:
            try:
                if not self.initialize():
                    return -1
            except Exception:
                return -1
                
        try:
            # Read sensor value
            sensor_value = GPIO.input(self.sensor_pin)
            return 1 if sensor_value == GPIO.HIGH else 0
        except Exception:
            return -1
            
    def __del__(self):
        """
        Destructor to ensure cleanup
        """
        self.cleanup()

# Example usage
if __name__ == "__main__":
    sensor = AM312Sensor()
    try:
        while True:
            result = sensor.detect()
            print(f"Detection result: {result}")
            time.sleep(1)
    except KeyboardInterrupt:
        sensor.cleanup()