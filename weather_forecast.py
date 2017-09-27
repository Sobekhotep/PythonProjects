import requests
import xml.etree.ElementTree as ET

class Forecast():
    """Weather forecast for city or town for which url is entered"""

    def __init__(self, url):
        self.url = url

    def today(self, night=False, morning=False, afternoon=False, evening=False):
        response = requests.get(self.url)
        root = ET.fromstring(response.text)
        if night == True:
            print('\nПрогноз погоды в г.', root[0][1].text,
                                   '\nна', root[0][4][0].text,
                ' \nТемпература воздуха:', root[0][4][2].text + ' градусов',
               '\nАтмосферное давление: ', root[0][4][1].text + ' мм ртутного столба')
        elif morning == True:
            print('\nПрогноз погоды в г.', root[0][1].text,
                                   '\nна', root[0][5][0].text,
                ' \nТемпература воздуха:', root[0][5][2].text + ' градусов',
               '\nАтмосферное давление: ', root[0][5][1].text + ' мм ртутного столба')
        elif afternoon == True:
            print('\nПрогноз погоды в г.', root[0][1].text,
                                   '\nна', root[0][6][0].text,
                ' \nТемпература воздуха:', root[0][6][2].text + ' градусов',
               '\nАтмосферное давление: ', root[0][6][1].text + ' мм ртутного столба')
        elif evening == True:
            print('\nПрогноз погоды в г.', root[0][1].text,
                                   '\nна', root[0][7][0].text,
                ' \nТемпература воздуха:', root[0][7][2].text + ' градусов',
               '\nАтмосферное давление: ', root[0][7][1].text + ' мм ртутного столба')
        else:
            print('Что-то пошло не так, звоните в милицию.')

    def tomorrow(self, night=False, morning=False, afternoon=False, evening=False):
        response = requests.get(self.url)
        root = ET.fromstring(response.text)
        if night == True:
            print('\nПрогноз погоды в г.', root[0][1].text,
                                   '\nна', root[0][8][0].text,
                ' \nТемпература воздуха:', root[0][8][2].text + ' градусов',
               '\nАтмосферное давление: ', root[0][8][1].text + ' мм ртутного столба')
        elif morning == True:
            print('\nПрогноз погоды в г.', root[0][1].text,
                                   '\nна', root[0][9][0].text,
                ' \nТемпература воздуха:', root[0][9][2].text + ' градусов',
               '\nАтмосферное давление: ', root[0][9][1].text + ' мм ртутного столба')
        elif afternoon == True:
            print('\nПрогноз погоды в г.', root[0][1].text,
                                   '\nна', root[0][10][0].text,
                ' \nТемпература воздуха:', root[0][10][2].text + ' градусов',
               '\nАтмосферное давление: ', root[0][10][1].text + ' мм ртутного столба')
        elif evening == True:
            print('\nПрогноз погоды в г.', root[0][1].text,
                                   '\nна', root[0][11][0].text,
                ' \nТемпература воздуха:', root[0][11][2].text + ' градусов',
               '\nАтмосферное давление: ', root[0][11][1].text + ' мм ртутного столба')
        else:
            print('Что-то пошло не так, звоните в милицию.')

    def after_tomorrow(self, night=False, morning=False, afternoon=False, evening=False):
        response = requests.get(self.url)
        root = ET.fromstring(response.text)
        if night == True:
            print('\nПрогноз погоды в г.', root[0][1].text,
                                   '\nна', root[0][12][0].text,
                ' \nТемпература воздуха:', root[0][12][2].text + ' градусов',
               '\nАтмосферное давление: ', root[0][12][1].text + ' мм ртутного столба')
        elif morning == True:
            print('\nПрогноз погоды в г.', root[0][1].text,
                                   '\nна', root[0][13][0].text,
                ' \nТемпература воздуха:', root[0][13][2].text + ' градусов',
               '\nАтмосферное давление: ', root[0][13][1].text + ' мм ртутного столба')
        elif afternoon == True:
            print('\nПрогноз погоды в г.', root[0][1].text,
                                   '\nна', root[0][14][0].text,
                ' \nТемпература воздуха:', root[0][14][2].text + ' градусов',
               '\nАтмосферное давление: ', root[0][14][1].text + ' мм ртутного столба')
        elif evening == True:
            print('\nПрогноз погоды в г.', root[0][1].text,
                                   '\nна', root[0][15][0].text,
                ' \nТемпература воздуха:', root[0][15][2].text + ' градусов',
               '\nАтмосферное давление: ', root[0][15][1].text + ' мм ртутного столба')
        else:
            print('Что-то пошло не так, звоните в милицию.')


forecast = Forecast('http://www.eurometeo.ru/belarus/gomelskaya-oblast/jitkovichi/export/xml/data/')
print(forecast.after_tomorrow(evening=True))