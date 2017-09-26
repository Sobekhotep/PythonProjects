import requests
import xml.etree.ElementTree as ET

class Forecast():

    def __init__(self, forecast):
        self.forecast = forecast
        self


    def forecast(self, url = 'http://www.eurometeo.ru/belarus/gomelskaya-oblast/jitkovichi/'
                        'export/xml/data/'):
        response = requests.get(url)
        root = ET.fromstring(response.text)

    def forecast_day(self, today = True, tomorrow = False, after_tomorrow = False):
        day_dict = {today: 1, tomorrow: 2, after_tomorrow: 3}
        if day in day_dict:
            pass
        else:
            print('Такого дня, к сожалению, нет.')
            raise SystemExit(1)

    def forecast_time(self, morning = True, afternoon = False, evening = False, night = False):
        time_dict = {morning: 1, afternoon: 2, evening: 3, night: 4}
        if day in time_dict:
            pass
        else:
            print('Такого времени, к сожалению, нет.')
            raise SystemExit(1)

    def
print ('\nТемпература воздуха:', root[0][day * 4 + time - 1][2].text + ' градусов',
           '\nАтмосферное давление: ', root[0][day * 4 + time - 1][1].text + ' мм ртутного столба')
