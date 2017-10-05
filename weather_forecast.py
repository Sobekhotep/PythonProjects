import requests
import xml.etree.ElementTree as ET


class ForecastResult():
    def __init__(self, temperature, pressure, result):
        self.temperature = temperature
        self.pressure = pressure
        self.result = result


class ForecastFetcher():
    """Weather forecast for city or town for which url is entered"""

    def __init__(self, url):
        self.url = url

    def forecast_fetcher(self, day, night=False, morning=False, afternoon=False, evening=False):

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
            print('Что-то пошло не так.')
            raise SystemExit(1)

        root_city = root[0][1].text
        root_time = root[0][day*4 + int(night)*night_value + int(morning)*morning_value +
                            int(afternoon)*afternoon_value + int(evening)*evening_value - 1][0].text
        root_temp = root[0][day*4 + int(night)*night_value + int(morning)*morning_value +
                            int(afternoon)*afternoon_value + int(evening)*evening_value - 1][2].text
        root_press = root[0][day*4 + int(night)*night_value + int(morning)*morning_value +
                            int(afternoon)*afternoon_value + int(evening)*evening_value - 1][1].text

        forecast_result = '\nПрогноз погоды по г. {}, \nна {}. \nТемпература воздуха: {} градусов. ' \
                  '\nАтмосферное давление: {} мм ртутного столба.'\
                  .format(root_city, root_time, root_temp, root_press)

        return ForecastResult(temperature=root_temp, pressure=root_press, result=forecast_result)

    def today(self, **kwargs):
        return self.forecast_fetcher(day=1, **kwargs)

    def tomorrow(self, **kwargs):
        return self.forecast_fetcher(day=2, **kwargs)

    def after_tomorrow(self, **kwargs):
        return self.forecast_fetcher(day=3, **kwargs)

forecast_fetcher = ForecastFetcher('http://www.eurometeo.ru/belarus/gomelskaya-oblast/jitkovichi/export/xml/data/')

result = forecast_fetcher.today(morning=True)
print(result.result)
print (ET.__doc__)