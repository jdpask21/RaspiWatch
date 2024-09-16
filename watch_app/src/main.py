import time
import board
import adafruit_dht as acd
import get_temperature_humidity as th


def main():

    dhtDevice = acd.DHT22(board.D18, use_pulseio=False)
    while True:
        try:
            temp, humidity = th.get_temp_hum(dhtDevice)
            print(
            "Temp: {:.1f} C    Humidity: {}% ".format(
                   temp, humidity
            )
            )
        except RuntimeError as error:
            print(0) 
        except Exception as error:
            dhtDevice.exit()
            dhtDevice = acd.DHT22(board.D18, use_pulseio=False)

        time.sleep(2.0)


if __name__ == "__main__":
    main()