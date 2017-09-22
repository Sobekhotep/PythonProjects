import requests
import xml.etree.ElementTree as ET

url = requests.get('http://www.eurometeo.ru/ukraina/kiyvska-oblast/kiyiv/export/xml/data/')
root = ET.fromstring(url.text)

day = int(input('На какой день Вы хотите узнать прогноз? Если на сегодня - введите цифру 1, '
          'на завтра - цифру 2, на послезавтра - цифру 3: '))

time = int(input('Какое время Вас интересует? Если утро - введите цифру 1, день - цифру 2, '
             'вечер - цифру 3, ночь - цифру 4: '))


if day == 1 and time == 1:
    print ('Давление: ', root[0][4][1].text, '\nТемпература:', root[0][4][2].text)
#elif day == 2 and time == 1:
#    print ('Давление: ', root[0][4][1].text, '\nТемпература:', root[0][4][2].text)
#    print ('Извините, прогноза погоды на такой день у нас нет, попробуйте ещё раз.')
