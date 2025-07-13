import spidev
import time

class MCP3002:
    def __init__(self, bus=0, device=0):
        """
        Initialize MCP3002 ADC converter
        
        @param  bus     SPI bus number (typically 0)
        @param  device  Device number (CE0=0, CE1=1)
        """
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
        
        # Configure SPI settings
        self.spi.max_speed_hz = 1000000  # 1MHz
        self.spi.mode = 0  # SPI mode 0 (CPOL=0, CPHA=0)
        
    def read_channel(self, channel):
        """
        Read AD value from specified channel
        
        @param  channel  Channel number (0 or 1)
        
        @retval adc_value  10-bit AD conversion value (0-1023)
        
        @exception ValueError  If channel is not 0 or 1
        """
        if channel not in [0, 1]:
            raise ValueError("Channel must be 0 or 1")
        
        # MCP3002 command format
        # Start bit (1) + Single/Diff (1) + Channel (1) + MSBF (1) + 4 dummy bits
        command = 0x68 if channel == 0 else 0x78  # 0x68 = ch0, 0x78 = ch1
        
        # Send/receive data via SPI (3 bytes)
        response = self.spi.xfer2([command, 0x00])
        
        # Extract 10-bit value from received data
        # Combine lower 2 bits of 2nd byte with upper 8 bits of 3rd byte
        adc_value = ((response[0] & 0x03) << 8) | response[1]
        
        return adc_value
    
    def read_voltage(self, channel, vref=3.3):
        """
        Read voltage value from specified channel
        
        @param  channel  Channel number (0 or 1)
        @param  vref     Reference voltage (default: 3.3V)
        
        @retval voltage  Voltage value in volts
        """
        adc_value = self.read_channel(channel)
        voltage = (adc_value * vref) / 1024.0
        return voltage
    
    def close(self):
        """
        Close SPI connection
        """
        self.spi.close()

def main():
    """
    Main function to test MCP3002 ADC converter
    """
    # Initialize MCP3002 (using CE0)
    adc = MCP3002(bus=0, device=0)
    
    try:
        print("MCP3002 ADC converter test started")
        print("Press Ctrl+C to exit")
        
        while True:
            # Read CDS sensor value from channel 0
            cds_adc_value = adc.read_channel(0)
            cds_voltage = adc.read_voltage(0)
            
            print(f"CDS Sensor - AD value: {cds_adc_value:4d}, Voltage: {cds_voltage:.3f}V")
            
            # If using channel 1 as well
            # ch1_adc_value = adc.read_channel(1)
            # ch1_voltage = adc.read_voltage(1)
            # print(f"Channel 1 - AD value: {ch1_adc_value:4d}, Voltage: {ch1_voltage:.3f}V")
            
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        adc.close()

if __name__ == "__main__":
    main()