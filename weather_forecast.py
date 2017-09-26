import requests
import xml.etree.ElementTree as ET

class Forecast():
    """Weather forecast for city or town for which url is entered"""

    def __init__(self, url, response, root, forecast_day, forecast_time):
        self.url = url
        self.response = response
        self.root = root
        self.forecast_day = forecast_day
        self.forecast_time = forecast_time

    def forecast(self, url = 'http://www.eurometeo.ru/belarus/gomelskaya-oblast/jitkovichi/'
                        'export/xml/data/'):
        response = requests.get(url)
        root = ET.fromstring(response.text)
        return root

    def forecast_day(self, today = True, tomorrow = False, after_tomorrow = False):
        day_dict = {today: 1, tomorrow: 2, after_tomorrow: 3}
        if day in day_dict:
            return day
        else:
            print('Такого дня, к сожалению, нет.')
            raise SystemExit(1)

    def forecast_time(self, morning=True, afternoon=False, evening=False, night=False):
        time_dict = {morning: 1, afternoon: 2, evening: 3, night: 4}
        if time in time_dict:
            return time
        else:
            print('Такого времени, к сожалению, нет.')
            raise SystemExit(1)

