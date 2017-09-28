import requests
import xml.etree.ElementTree as ET

DAY_LIST = (1, 2, 3)

NIGHT_VALUE = 1
MORNING_VALUE = 2
AFTERNOON_VALUE = 3
EVENING_VALUE = 4

class Forecast():
    """Weather forecast for city or town for which url is entered"""

    def __init__(self, url):
        self.url = url

    def forecast(self, day, night=False, morning=False, afternoon=False, evening=False):
        response = requests.get(self.url)
        root = ET.fromstring(response.text)
        if day in DAY_LIST:
            pass
        else:
            print('Что-то пошло не так, звоните в милицию.')
            raise SystemExit(1)

        root_city = root[0][1].text
        root_time = root[0][day*4 + int(night)*NIGHT_VALUE + int(morning)*MORNING_VALUE +
                            int(afternoon)*AFTERNOON_VALUE + int(evening)*EVENING_VALUE - 1][0].text
        root_temp = root[0][day*4 + int(night)*NIGHT_VALUE + int(morning)*MORNING_VALUE +
                            int(afternoon)*AFTERNOON_VALUE + int(evening)*EVENING_VALUE - 1][2].text
        root_press = root[0][day*4 + int(night)*NIGHT_VALUE + int(morning)*MORNING_VALUE +
                            int(afternoon)*AFTERNOON_VALUE + int(evening)*EVENING_VALUE - 1][1].text

        text1 = "Прогноз погоды по г. "
        text2 = " на "
        text3 = " Температура воздуха: "
        text4 = " градусов. "
        text5 = " Атмосферное давление: "
        text6 = " мм ртутного столба."

        message = text1 + str(root_city) + text2 + str(root_time) + text3 + str(root_temp) \
                  + text4 + text5 + str(root_press) + text6

        return message

    def today(self, night=False, morning=False, afternoon=False, evening=False):
        return self.forecast(day=1, night=night, morning=morning, afternoon=afternoon, evening=evening)

    def tomorrow(self, night=False, morning=False, afternoon=False, evening=False):
        return self.forecast(day=2, night=night, morning=morning, afternoon=afternoon, evening=evening)

    def after_tomorrow(self, night=False, morning=False, afternoon=False, evening=False):
        return self.forecast(day=3, night=night, morning=morning, afternoon=afternoon, evening=evening)

forecast = Forecast('http://www.eurometeo.ru/belarus/gomelskaya-oblast/jitkovichi/export/xml/data/')
print(forecast.today(night=True))