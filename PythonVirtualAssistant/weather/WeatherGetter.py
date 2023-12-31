﻿from bs4 import BeautifulSoup
import requests

class WeatherGetter:

    @staticmethod
    def get_Tomsk_weather():
        try:
            print("Загрузка...")

            res = requests.get(f'https://pogodavtomske.ru/&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8')

            soup = BeautifulSoup(res.text, 'html.parser')
            temperature = soup.select('#temp')[0].getText().strip()

            print('Температура в Томске ' + temperature)

        except Exception as er:
            print("Не найдено")
            print(f'Error: {er}')


    @staticmethod
    def get_weather_scheme(city_name: str):
        url = 'https://wttr.in/{}'.format(city_name)
        res = requests.get(url)
        print(res.text.replace('Follow [46m[30m@igor_chubin[0m for wttr.in updates', ''))

