# weather/views.py
import requests
from django.shortcuts import render
from django.http import HttpResponse

def get_temperature(request):
    if request.method == "POST":
        city = request.POST.get('city')
        if city:
            api_key = 'b65ff0940dfde6a3283d2d7ccfdd8a17'  # replace with your actual API key
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            response = requests.get(url)
            data = response.json()
            if data.get('cod') != 200:
                context = {'error': data.get('message')}
            else:
                temperature = data['main']['temp']
                context = {'city': city, 'temperature': temperature}
            return render(request, 'weather/temperature.html', context)
    return render(request, 'weather/temperature.html')
