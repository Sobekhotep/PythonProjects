import requests
import xml.etree.ElementTree as ET


class ForecastResult():
    def __init__(self, url):
        self.url = url

    def __str__(self):
        response = requests.get(self.url)
        root = ET.fromstring(response.text)
        return root

class ForecastFetcher():
    """Weather forecast for city or town for which url is entered"""

    def __init__(self, url):
        self.url = url

    def forecast(self, day, night=False, morning=False, afternoon=False, evening=False):

        day_tuple = (1, 2, 3)
        night_value = 1
        morning_value = 2
        afternoon_value = 3
        evening_value = 4

        response = requests.get(self.url)
        root = ET.fromstring(response.text)
        if day in day_tuple:
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

        forecast_result = '\nПрогноз погоды по г. {}, на {}. \nТемпература воздуха: {} градусов. ' \
                  '\nАтмосферное давление: {} мм ртутного столба.'\
                  .format(root_city, root_time, root_temp, root_press)

        return forecast_result

    def today(self, **kwargs):
        return self.forecast(day=1, **kwargs)

    def tomorrow(self, **kwargs):
        return self.forecast(day=2, **kwargs)

    def after_tomorrow(self, **kwargs):
        return self.forecast(day=3, **kwargs)


forecast = ForecastFetcher('http://www.eurometeo.ru/belarus/gomelskaya-oblast/jitkovichi/export/xml/data/')
print(forecast.tomorrow(night=True))

forecast = ForecastResult('http://www.eurometeo.ru/belarus/gomelskaya-oblast/jitkovichi/export/xml/data/')
print(forecast.__str__())