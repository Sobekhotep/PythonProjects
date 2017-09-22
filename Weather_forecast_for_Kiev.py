import requests
import xml.etree.ElementTree as ET

url = requests.get('http://www.eurometeo.ru/ukraina/kiyvska-oblast/kiyiv/export/xml/data/')
root = ET.fromstring(url.text)

print ('Вас приветствует электронный синоптик города Киева, версия 1.0')

day = int(input('На какой день Вы хотите узнать прогноз погоды? Если на сегодня - введите цифру 1, '
          'на завтра - цифру 2, на послезавтра - цифру 3: '))

time = int(input('Какое время суток Вас интересует? Если утро - введите цифру 1, день - цифру 2, '
             'вечер - цифру 3, ночь - цифру 4: '))

if 0 < day < 4 and 0 < time < 5:
    print ('\nТемпература воздуха:', root[0][day*4+time-1][2].text + ' градусов', '\nАтмосферное давление: ', root[0][day*4+time-1][1].text + ' мм ртутного столба')
else:
    print ('\nХм, кто-то натыкал значений вне диапазона. Жаль.')