import requests
from django.shortcuts import render


def weather(request):
    city = 'Nairobi'
    api_key = '5b5ab0059182b6838eacb9390efe0753'  
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    data = response.json()

    weather_data = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'].capitalize(),
        'icon': data['weather'][0]['icon'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        
    }

    return render(request, 'templates/index.html', {'weather': weather_data})