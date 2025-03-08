import flet as ft
from dotenv import load_dotenv
import os
from src import get_now_time, get_weather
from src import get_temperature_humidity
from src import get_human_exist
from src import switch_bot
from src import get_light_sensor
import board
import adafruit_dht as acd
import time

WEATHER_UPDATE_MINUTES = 60 * 60 * 6
LIGHT_OFF_MINUTES = 60 * 10

celsius = ft.Text("℃", size=100, color=ft.colors.LIGHT_BLUE_50)
persent = ft.Text("%", size=100, color=ft.colors.LIGHT_BLUE_50)
wb_sunny = ft.Icon(name=ft.icons.WB_SUNNY, color=ft.colors.WHITE, size=700)
wb_cloudy = ft.Icon(name=ft.icons.WB_CLOUDY, color=ft.colors.WHITE, size=700)
wb_rainy = ft.Icon(name=ft.icons.WATER_DROP, color=ft.colors.WHITE, size=700)
wb_sunny_and_cloudy = ft.Icon(name=ft.icons.WB_TWIGHLIGHT, color=ft.colors.WHITE, size=700)
wb_cloudy_and_rainy = ft.Icon(name=ft.icons.WATER, color=ft.colors.WHITE, size=700)
wb_unknown = ft.Icon(name=ft.icons.LOCATION_DISABLED_ROUNDED, color=ft.colors.WHITE, size=700)
light_icon_ = ft.Icon(name=ft.icons.WB_TWIGHLIGHT, color=ft.colors.WHITE, size=200)
light_off_icon_ = ft.Icon(name=ft.icons.NIGHTLIGHT, color=ft.colors.WHITE, size=200)


def load_switchbot_credentials():
    """
    Load SwitchBot credentials from environment variables
    """
    # Load environment variables from .env file if it exists
    load_dotenv()

    # Get environment variables
    api_token = os.getenv('SWITCHBOT_API_TOKEN')
    api_secret = os.getenv('SWITCHBOT_API_SECRET')
    device_id = os.getenv('SWITCHBOT_DEVICE_ID')

    if not all([api_token, api_secret, device_id]):
        raise EnvironmentError("Missing required environment variables")

    return {
        'token': api_token,
        'secret': api_secret,
        'device_id': device_id
    }

def change_light_status_by_Cds(count_light_status_diff: int, light_status: str):
    count_light_status_diff += 1
    if count_light_status_diff == 3:
        count_light_status_diff = 0
        if light_status == "ON":
            return "OFF", count_light_status_diff
        else:
            return "ON", count_light_status_diff
    return light_status, count_light_status_diff

def initialize_each_param():
    return False, 0, 0

def main(page: ft.Page):
    dhtDevice = acd.DHT22(board.D18, use_pulseio=False)
    pir_sensor = get_human_exist.AM312Sensor()
    light_sensor = get_light_sensor.GL5528Sensor(gpio_pin=21)
    light_status = "ON"
    start_count = False
    passed_seconds = 0
    ref_time = 0
    count_light_status_diff = 0

    def get_str_time():
        now_hour, now_minute, month_day, weekday, dt = get_now_time.get_now_time()
        return "{}:{:02}".format(now_hour, now_minute), month_day, weekday, dt
    
    def get_weather_icon():
        wb_code = get_weather.get_osaka_weather()
        if wb_code == 1:
            return wb_sunny
        elif wb_code == 2:
            return wb_cloudy
        elif wb_code == 3:
            return wb_rainy
        elif wb_code == 4:
            return wb_sunny_and_cloudy
        elif wb_code == 5:
            return wb_cloudy_and_rainy
        elif wb_code == 6:
            return wb_unknown
    
    def turn_on_light():
        controller = switch_bot.SwitchBotController(SWITCHBOT_API_TOKEN, SWITCHBOT_API_SECRET, SWITCHBOT_DEVICE_ID)
        light_on_result = controller.turn_on_light()

    page.title = "Custom fonts"
    page.fonts = {
        "NnumGothic": "fonts/NanumGothic-ExtraBold.ttf",
    }

    page.theme = ft.Theme(font_family="NnumGothic")

    now_time, month_day, weekday, dt = get_str_time()
    temp = 0
    humidity = 0
    
    display_time = ft.Text(str(now_time), size=600, color=ft.colors.BLUE_300)
    display_month = ft.Text(str(month_day), size=140, color=ft.colors.WHITE)
    display_weekday = ft.Text(str(weekday), size=150, color=ft.colors.BLUE_600)
    display_temp = ft.Text(str(temp), size=150, color=ft.colors.LIGHT_BLUE_50)
    display_humidity = ft.Text(str(humidity), size=150, color=ft.colors.LIGHT_BLUE_50)
    weather = ft.Container(
                content=get_weather_icon(),
                margin=0,
                padding=0,
                alignment=ft.Alignment(-0.8, 0.2),
                bgcolor=ft.colors.TRANSPARENT,
                width=1000,
                height=500,
            )
    old_time = dt

    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0
    page.margin = 0
    page.spacing = 0
    page.window.full_screen=True
    page.add(
        ft.Column(
            controls = [
                ft.Stack(
                    [
                        ft.Row(
                            controls = [
                                weather,
                                ],
                        ),
                        ft.Container(
                            content=display_time,
                            margin=0,
                            padding=0,
                            alignment=ft.Alignment(0, -1),
                            bgcolor=ft.colors.TRANSPARENT,
                            width=2000,
                            height=700,
                        ),
                    ]
                ),
                ft.Row(
                    controls = [
                        ft.Container(
                            content=display_temp,
                            margin=0,
                            padding=0,
                            alignment=ft.Alignment(-1, 0),
                            bgcolor=ft.colors.BLACK,
                            width=350,
                            height=300,
                        ),
                        ft.Container(
                            content=celsius,
                            margin=0,
                            padding=0,
                            alignment=ft.Alignment(-0.65, 0),
                            bgcolor=ft.colors.BLACK,
                            width=150,
                            height=300,
                        ),
                        ft.Container(
                            content=display_humidity,
                            margin=0,
                            padding=0,
                            alignment=ft.Alignment(-0.5, 0),
                            bgcolor=ft.colors.BLACK,
                            width=350,
                            height=300,
                        ),
                        ft.Container(
                            content=persent,
                            margin=0,
                            padding=0,
                            alignment=ft.Alignment(-0.15, 0),
                            bgcolor=ft.colors.BLACK,
                            width=150,
                            height=300,
                        ),
                        ft.Container(
                            content=display_month,
                            margin=0,
                            padding=0,
                            alignment=ft.Alignment(0.3, 0),
                            bgcolor=ft.colors.BLACK,
                            width=400,
                            height=300,
                        ),
                        ft.Container(
                            content=display_weekday,
                            margin=0,
                            padding=0,
                            alignment=ft.Alignment(0.6, 0),
                            bgcolor=ft.colors.BLACK,
                            width=500,
                            height=300,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=0,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=0,
        ),
    )

    while True:
        try:
            now_temp, now_humidity = get_temperature_humidity.get_temp_hum(dhtDevice)
            display_temp.value = now_temp
            display_humidity.value = now_humidity
        except RuntimeError as error:
            pass
        except Exception:
            dhtDevice = acd.DHT22(board.D18, use_pulseio=False)
        
        display_time.value, display_month.value, display_weekday.value, dt = get_str_time()

        # 天気の更新頻度は6時間に1回
        if (dt - old_time).seconds >= WEATHER_UPDATE_MINUTES:
            try:
                weather.content = get_weather_icon()
            except Exception:
                weather.content = wb_unknown
            old_time = dt
        else:
            pass
        
        light_result = light_sensor.read_brightness()
        if (light_result and light_status == "OFF") or (not light_result and light_status == "ON"):
            light_status, count_light_status_diff = change_light_status_by_Cds(count_light_status_diff, light_status)
        if light_status == "ON":
            light_icon.content = light_icon_
        else:
            light_icon.content = light_off_icon_
        ##
        # @brief Light control module with AM312 PIR sensor
        # @details This module controls light based on human presence detection:
        #          - When light_status is ON:
        #            Turn off the light if no human is detected for 10 minutes or more
        #          - When light_status is OFF:
        #            Turn on the light when human is detected
        ##
        pir_result = pir_sensor.detect()
        if not pir_result and light_status == "ON" and not start_count:
            start_count = True
            ref_time = time.time()
            passed_seconds = 0
        elif not pir_result and light_status == "ON" and start_count:
            passed_seconds = time.time() - ref_time
            if passed_seconds >= LIGHT_OFF_MINUTES:
                turn_on_light()
                light_status = "OFF"
                start_count, ref_time, passed_seconds = initialize_each_param()
        elif pir_result and light_status == "ON":
            if start_count:
                start_count, ref_time, passed_seconds = initialize_each_param()
        elif pir_result and light_status == "OFF":
            turn_on_light()
            light_status = "ON"
        elif not pir_result and light_status == "OFF":
            start_count, ref_time, passed_seconds = initialize_each_param()
        else:
            pass
        page.update()
        time.sleep(1.0)

credentials = load_switchbot_credentials()
SWITCHBOT_API_TOKEN = credentials['token']
SWITCHBOT_API_SECRET = credentials['secret']
SWITCHBOT_DEVICE_ID = credentials['device_id']
ft.app(target=main, assets_dir="assets")
