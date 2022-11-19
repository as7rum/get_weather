import requests
import datetime
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):
    
    code_to_smile = {
           'Clear': 'Ясно \N{black sun with rays}',
           'Clouds': 'Облачно \N{sun behind cloud}',
           'Rain': 'Дождь \N{umbrella with rain drops}',
           'Drizzle': 'Дождь \N{umbrella with rain drops}',
           'Thunderstorm': 'Гроза \N{high voltage sign}',
           'Snow': 'Снег \N{snowflake}',
           'Mist': 'Туман \N{foggy}',

    }
    
    
    
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric')
        
        data = r.json()
        #pprint(data)

        city = data['name']

        weather_discription = data['weather'][0]['main']

        if weather_discription in code_to_smile:
            wd = code_to_smile[weather_discription]
        else:
            wd = 'Лучше выгляни ка в окно...'

        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = sunset_timestamp - sunrise_timestamp

        print(#f'___{datetime.datetime.now().strftime('%d')}___\n'
              f'Погода в {city}:\n {wd}\nТемпература: {cur_weather}C°\n'
              f'Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст.\nВетер: {wind} м/с\n'
              f'Восход солнца: {sunrise_timestamp}\nЗаход солнца: {sunset_timestamp}\n'
              f'Продолжительность дня: {length_of_the_day}\n'
              f'Хорошего дня!')

    
    except Exception as ex:
        print(ex)
        print('Проверьте название города')

def main():
    city = input('Введите город: ')
    get_weather(city, open_weather_token)

if __name__ == '__main__':
   main()