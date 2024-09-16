import flet as ft
from src import get_now_time
from src import get_temperature_humidity
import board
import adafruit_dht as acd
import time


def main(page: ft.Page):
    dhtDevice = acd.DHT22(board.D18, use_pulseio=False)
    def get_str_time():
        now_hour, now_minute, month_day, weekday = get_now_time.get_now_time()
        return "{}:{:02}".format(now_hour, now_minute), month_day, weekday

    page.title = "Custom fonts"
    page.fonts = {
        "NnumGothic": "fonts/NanumGothic-ExtraBold.ttf",
    }

    page.theme = ft.Theme(font_family="NnumGothic")

    now_time, month_day, weekday = get_str_time()
    temp = 0
    humidity = 0
    
    display_time = ft.Text(str(now_time), size=600, color=ft.colors.BLUE_300)
    display_month = ft.Text(str(month_day), size=150, color=ft.colors.WHITE)
    display_weekday = ft.Text(str(weekday), size=150, color=ft.colors.BLUE_600)
    display_temp = ft.Text(str(temp), size=150, color=ft.colors.LIGHT_BLUE_50)
    display_humidity = ft.Text(str(humidity), size=150, color=ft.colors.LIGHT_BLUE_50)
    celsius = ft.Text("℃", size=100, color=ft.colors.LIGHT_BLUE_50)
    persent = ft.Text("%", size=100, color=ft.colors.LIGHT_BLUE_50)

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
                ft.Container(
                    content=display_time,
                    margin=0,
                    padding=0,
                    alignment=ft.Alignment(0, -1),
                    bgcolor=ft.colors.BLACK,
                    width=2000,
                    height=700,
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
        
        display_time.value, display_month.value, display_weekday.value = get_str_time()
        page.update()
        time.sleep(2.0)
        
ft.app(target=main, assets_dir="assets")
