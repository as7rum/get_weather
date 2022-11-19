# Get Weather

This code takes city name and returns `json` format current weather. After that it creates a message with temperature, humidity, pressure and etc. 

It works with [OpenWeatherMap](https://openweathermap.org/) API, so get your API token before the start. 

## Tips

You can uncomment `pprint` string and check json output. 

```python
 data = r.json()
 #pprint(data)
```

Don't forget comment the next code before (Use `Cmd + /`):

```python
 city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = sunset_timestamp - sunrise_timestamp

        print(f'Погода в {city}:\nТемпература: {cur_weather}C\n'
              f'Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст.\nВетер: {wind} м/с\n'
              f'Восход солнца: {sunrise_timestamp}\nЗаход солнца: {sunset_timestamp}\n'
              f'Продолжительность дня: {length_of_the_day}\n'
              f'Хорошего дня!')
```

If you want to get Kelvin tempreture format delete `units` part from link here:

```python
 r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric')
```

## Last word 

Have a success! See you. 

`Let's bring this world to the Horizon!`
