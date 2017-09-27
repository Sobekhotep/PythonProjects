import requests
import xml.etree.ElementTree as ET

day_list = [1, 2, 3]
time_list = [1, 2, 3, 4]

night_value = 1
morning_value = 2
afternoon_value = 3
evening_value = 4

class Forecast():
    """Weather forecast for city or town for which url is entered"""

    def __init__(self, url):
        self.url = url

    def today(self, night=False, morning=False, afternoon=False, evening=False):
        response = requests.get(self.url)
        root = ET.fromstring(response.text)
        root_city = root[0][1].text
        root_time = root[0][4 + int(night)*night_value + int(morning)*morning_value +
                            int(afternoon)*afternoon_value + int(evening)*evening_value - 1][0].text
        root_temp = root[0][4 + int(night)*night_value + int(morning)*morning_value +
                            int(afternoon)*afternoon_value + int(evening)*evening_value - 1][2].text
        root_press = root[0][4 + int(night)*night_value + int(morning)*morning_value +
                             int(afternoon)*afternoon_value + int(evening)*evening_value - 1][1].text

        print ('\nПрогноз погоды по г.', root_city,
                                '\nна', root_time,
             ' \nТемпература воздуха:', root_temp + ' градусов',
            '\nАтмосферное давление: ', root_press + ' мм ртутного столба')
        return ('Спасибо!')

    def tomorrow(self, night=False, morning=False, afternoon=False, evening=False):
        response = requests.get(self.url)
        root = ET.fromstring(response.text)
        root_city = root[0][1].text
        root_time = root[0][8 + int(night)*night_value + int(morning)*morning_value +
                            int(afternoon)*afternoon_value + int(evening)*evening_value - 1][0].text
        root_temp = root[0][8 + int(night)*night_value + int(morning)*morning_value +
                            int(afternoon)*afternoon_value + int(evening)*evening_value - 1][2].text
        root_press = root[0][8 + int(night)*night_value + int(morning)*morning_value +
                             int(afternoon)*afternoon_value + int(evening)*evening_value - 1][1].text

        print ('\nПрогноз погоды по г.', root_city,
                                '\nна', root_time,
             ' \nТемпература воздуха:', root_temp + ' градусов',
            '\nАтмосферное давление: ', root_press + ' мм ртутного столба')
        return ('Спасибо!')

    def after_tomorrow(self, night=False, morning=False, afternoon=False, evening=False):
        response = requests.get(self.url)
        root = ET.fromstring(response.text)
        root_city = root[0][1].text
        root_time = root[0][12 + int(night)*night_value + int(morning)*morning_value +
                            int(afternoon)*afternoon_value + int(evening)*evening_value - 1][0].text
        root_temp = root[0][12 + int(night)*night_value + int(morning)*morning_value +
                            int(afternoon)*afternoon_value + int(evening)*evening_value - 1][2].text
        root_press = root[0][12 + int(night)*night_value + int(morning)*morning_value +
                             int(afternoon)*afternoon_value + int(evening)*evening_value - 1][1].text

        print ('\nПрогноз погоды по г.', root_city,
                                '\nна', root_time,
             ' \nТемпература воздуха:', root_temp + ' градусов',
            '\nАтмосферное давление: ', root_press + ' мм ртутного столба')
        return ('Спасибо!')

    def forecast(self, day, night=False, morning=False, afternoon=False, evening=False):
        response = requests.get(self.url)
        root = ET.fromstring(response.text)
        if day in day_list:
            pass
        else:
            print('Что-то пошло не так, звоните в милицию.')
            raise SystemExit(1)

        root_city = root[0][1].text
        root_time = root[0][day*4 + int(night)*night_value + int(morning)*morning_value +
                            int(afternoon)*afternoon_value + int(evening)*evening_value - 1][0].text
        root_temp = root[0][day*4 + int(night)*night_value + int(morning)*morning_value +
                            int(afternoon)*afternoon_value + int(evening)*evening_value - 1][2].text
        root_press = root[0][day*4 + int(night)*night_value + int(morning)*morning_value +
                             int(afternoon)*afternoon_value + int(evening)*evening_value - 1][1].text

        print ('\nПрогноз погоды по г.', root_city,
                                '\nна', root_time,
             ' \nТемпература воздуха:', root_temp + ' градусов',
            '\nАтмосферное давление: ', root_press + ' мм ртутного столба')
        return ('Спасибо!')

forecast = Forecast('http://www.eurometeo.ru/belarus/gomelskaya-oblast/jitkovichi/export/xml/data/')
print(forecast.forecast(day=2, evening = True))