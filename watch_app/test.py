from src import get_human_exist
from src import switch_bot
import time
pir_sensor = get_human_exist.AM312Sensor()
light_status = "ON"
start_count = False
passed_seconds = 0
ref_time = 0

THIRTY_MINUTES = 30

SWITCHBOT_API_TOKEN = 'f42f155084a932a17beecdd725b74c3fe9c5035d46d6393b3f4741bc9834a92d7842ecb170c85c191007225705e634a5'
SWITCHBOT_API_SECRET = '2303a5207d6e350b9b05f1f39748d3e0'
SWITCHBOT_DEVICE_ID = '02-202407131858-36105809'

def turn_on_light():
    controller = switch_bot.SwitchBotController(SWITCHBOT_API_TOKEN, SWITCHBOT_API_SECRET, SWITCHBOT_DEVICE_ID)
    light_on_result = controller.turn_on_light()

def initialize_countdown():
    ref_time = 0
    start_count = False
    passed_seconds = 0
# @brief Light control module with AM312 PIR sensor
# @details This module controls light based on human presence detection:
#          - When light_status is ON:
#            Turn off the light if no human is detected for 30 minutes or more
#          - When light_status is OFF:
#            Turn on the light when human is detected
##
while True:
    pir_result = pir_sensor.detect()
    # print(pir_result)
    # turn off the light
    if not pir_result and light_status == "ON" and not start_count:
        start_count = True
        ref_time = time.time()
        passed_seconds = 0
        print(1, light_status)
    elif not pir_result and light_status == "ON" and start_count:
        passed_seconds = time.time() - ref_time
        print(2, light_status)
        if passed_seconds >= THIRTY_MINUTES:
            # turn_on_light()
            light_status = "OFF"
            start_count = False
            ref_time = 0
            passed_seconds = 0
            print(3, light_status)
    elif pir_result and light_status == "ON":
        print(4, light_status)
        if start_count:
            initialize_countdown()
            print(5, light_status)
    elif pir_result and light_status == "OFF":
        # turn_on_light()
        light_status = "ON"
        print(6, light_status)
    else:
        print(7, light_status)
        pass
    time.sleep(1)