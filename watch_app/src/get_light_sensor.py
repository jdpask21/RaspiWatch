import RPi.GPIO as GPIO
import time

class GL5528Sensor:
    """
    ## @class GL5528Sensor
    #  @brief
    Class to interact with the GL5528 Cds sensor.
    
    #  @details
    This class handles GPIO initialization, brightness reading, and cleanup.
    It allows setting the GPIO pin at instantiation.
    """
    
    def __init__(self, gpio_pin):
        """
        ## @brief
        Initializes the GL5528Sensor class with a specified GPIO pin.
        
        ## @param gpio_pin GPIO pin number connected to the Cds sensor.
        """
        self.gpio_pin = gpio_pin
        
        # Initialize GPIO settings
        self.init_gpio()

    def init_gpio(self):
        """
        ## @brief
        Initializes GPIO settings for the Cds sensor.
        
        ## @details
        Sets the GPIO mode to BCM and configures the specified pin as input.
        """
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.gpio_pin, GPIO.IN)
        except Exception as e:
            print(f"Error during GPIO initialization: {e}")
            GPIO.cleanup()
            raise

    def read_brightness(self):
        """
        ## @brief
        Reads brightness from the Cds sensor.
        
        ## @details
        Checks the digital input from the specified GPIO pin.
        
        ## @retval 1 Room is bright.
        ## @retval 0 Room is dark.
        """
        try:
            # Read digital input from Cds sensor
            if GPIO.input(self.gpio_pin) == GPIO.HIGH:
                # print("Room is bright.")
                return 1
            else:
                # print("Room is dark.")
                return 0
        except Exception as e:
            print(f"Error reading from Cds sensor: {e}")
            GPIO.cleanup()
            raise

    def cleanup(self):
        """
        ## @brief
        Cleans up the GPIO settings.
        
        ## @details
        Resets the GPIO configuration to avoid conflicts.
        """
        GPIO.cleanup()

# Main loop to continuously check brightness
def main():
    """
    ## @brief
    Main loop to check the brightness continuously.
    
    ## @details
    Reads brightness every second until interrupted.
    """
    # Create an instance of GL5528Sensor with GPIO pin 21
    sensor = GL5528Sensor(gpio_pin=21)
    
    try:
        while True:
            sensor.read_brightness()
            time.sleep(1)  # Check every second
    except KeyboardInterrupt:
        print("Terminating the program...")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        # Cleanup GPIO settings
        sensor.cleanup()

# Entry point
if __name__ == "__main__":
    main()
