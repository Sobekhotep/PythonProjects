import requests
import xml.etree.ElementTree as ET


class ForecastResult():
    def __init__(self, temperature, pressure, get_temperature_cel, get_temperature_far,
        get_pressure_mmhg, get_pressure_pascal):
        self.temperature = temperature
        self.pressure = pressure
        self.get_temperature_cel = get_temperature_cel
        self.get_temperature_far = get_temperature_far
        self.get_pressure_mmhg = get_pressure_mmhg
        self.get_pressure_pascal = get_pressure_pascal


    def __str__(self):
        return str(self.temperature) + '\n' + str(self.pressure)


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
        temperature_cel = root_temp
        temperature_far = round(float(root_temp)*1.8 + 32, 1)
        pressure_mmhg = root_press
        pressure_pascal = round(float(root_press)*133.322, 1)

        return ForecastResult(temperature=root_temp, pressure=root_press,
                              get_temperature_cel=temperature_cel,
                              get_temperature_far=temperature_far,
                              get_pressure_mmhg=pressure_mmhg,
                              get_pressure_pascal=pressure_pascal)

    def today(self, **kwargs):
        return self.forecast_fetcher(day=1, **kwargs)

    def tomorrow(self, **kwargs):
        return self.forecast_fetcher(day=2, **kwargs)

    def after_tomorrow(self, **kwargs):
        return self.forecast_fetcher(day=3, **kwargs)

forecast_fetcher = ForecastFetcher('http://www.eurometeo.ru/belarus/gomelskaya-oblast/jitkovichi/export/xml/data/')

result = forecast_fetcher.after_tomorrow(afternoon=True)
print(result.get_pressure_mmhg)
