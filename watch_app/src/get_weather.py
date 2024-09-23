import requests
from bs4 import BeautifulSoup
import flet as ft

sunny = ["晴れ"]
cloudy = ["曇り"]
rainy = ["雨", "雨時々曇", "雨時々晴", "雨一時曇", "雨一時晴"]
sunny_and_cloudy = ["曇時々晴", "晴時々曇", "曇のち晴", "晴のち曇"]
cloudy_and_rainy = ["曇時々雨", "晴時々雨", "曇のち雨", "雨のち曇",
                    "晴のち雨", "曇のち雨", "曇一時雨", "晴一時雨"]

def get_osaka_weather():
    # Yahoo天気の大阪市のURL
    url = "https://weather.yahoo.co.jp/weather/jp/27/6200.html"
    # Yahoo天気那覇市のURL
    # url = "https://weather.yahoo.co.jp/weather/jp/47/9110.html"    
    # HTTPリクエストを送信
    response = requests.get(url)
    
    # レスポンスが正常か確認
    if response.status_code == 200:
        # BeautifulSoupでHTMLを解析
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 天気情報の取得
        weather_info = soup.find('div', class_='forecastCity').find('p', class_='pict').get_text()
        # temp_info = soup.find('span', class_='value')
        weather_info = weather_info.replace(" ", "").replace("\n", "")
        # print(weather_info)
        
        if weather_info in sunny:
            return 1
        elif weather_info in cloudy:
            return 2
        elif weather_info in rainy:
            return 3
        elif weather_info in sunny_and_cloudy:
            return 4
        elif weather_info in cloudy_and_rainy:
            return 5
        else:
            return 6
    else:
        raise Exception
    

if __name__ == "__main__":
    try:
        weather = get_osaka_weather()
        print(weather)
    except Exception as error:
        print("Yahoo天気のURLにアクセスできていない可能性があります。")
