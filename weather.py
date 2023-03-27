import requests
from time import sleep
text = 'Weather'
textpt = 'Temperatura'
api_key = '8a4372d9545e12dc13b26ded43a63c54'
while True:
    try:
        print('Select Language',)
        language = int(input('1 - Portuguese \n2 - English \nChoice: '))
    except:
        print('ERRO! Type just 1 or 2')
    else:
        break
if language == 1:
    for c in textpt:
        print(c, end='')
        sleep(0.4)
    print()
    while True:
        try:
            city = str(input('Nome da cidade: ')).strip().capitalize()
            r = requests.get(f'http://api.weatherstack.com/current?access_key={api_key}&query={city}')
            data = r.json()
            temperature = data['current']['temperature']
            print(f'A temperatura em {city} é de {temperature}°c')
            break
        except:
            print('ERRO! Reescreva o nome da cidade')
elif language == 2:
    for c in text:
        print(c, end='')
        sleep(0.4)
    print()
    while True:
        try:
            city = str(input('City name: ')).strip().capitalize()
            r = requests.get(f'http://api.weatherstack.com/current?access_key={api_key}&query={city}')
            data = r.json()
            temperature = data['current']['temperature']
            print(f'Current temperature of {city} is {temperature}°c')
            break
        except:
            print('ERROR! Rewrite the city name')