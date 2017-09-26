import requests
import xml.etree.ElementTree as ET

response = requests.get('http://www.eurometeo.ru/belarus/gomelskaya-oblast/jitkovichi/export/xml/data/')
root = ET.fromstring(response.text)

print ('Вас приветствует электронный синоптик города Житковичи, версия 1.0')

day = int(input('На какой день Вы хотите узнать прогноз погоды? Если на сегодня - введите цифру 1, '
          'на завтра - цифру 2, на послезавтра - цифру 3: '))

day_list = [1, 2, 3]
time_list = [1, 2, 3, 4]

if day in day_list:
    pass
else:
    print ('Такого дня, к сожалению, нет.')
    raise SystemExit(1)

time = int(input('Какое время суток Вас интересует? Если утро - введите цифру 1, день - цифру 2, '
             'вечер - цифру 3, ночь - цифру 4: '))

if time in time_list:
    pass
else:
    print ('Такого времени, к сожалению, нет.')
    raise SystemExit(1)

root_temp = root[0][day * 4 + time - 1][2].text
root_press = root[0][day * 4 + time - 1][1].text

middle_teemp = round(root_temp)
temp = str(middle_temp)
press = str(root_press)

print ('\nТемпература воздуха:', temp + ' градусов',
          '\nАтмосферное давление: ', press + ' мм ртутного столба')