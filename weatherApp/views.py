from django.shortcuts import render
import datetime
import requests
from django.contrib import messages
from django.http import HttpResponse




# Create your views here.
def index(request):
    try:
        apikey = open("D:\\HAZEL\\GITHUB\\WEATHER_FORECAST\\weatherApp\\apikey", "r").read()
        current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
        forecast_url = "https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}"
    
    
        if request.method == 'POST':
            city1 = request.POST['city1']
            city2 = request.POST.get('city2', None)
            
            weather_data1, daily_forecast1 = fetch_weather_and_forecast(city1.upper(), apikey,current_weather_url, forecast_url)
            if city2:
                weather_data2, daily_forecast2 = fetch_weather_and_forecast(city2.upper(), apikey,current_weather_url, forecast_url)
            else:
                weather_data2, daily_forecast2 = None, None
            context ={
                "weather_data1":weather_data1,
                "daily_forecast1":daily_forecast1,
                "weather_data2":weather_data2,
                "daily_forecast2":daily_forecast2,
            }
            return render(request, 'index.html', context)
                
        else:
            return render(request, "index.html")
    except requests.exceptions.ConnectionError:
        return HttpResponse("Please Connect to the Internet")    
    
def fetch_weather_and_forecast(city,apikey, current_weather_url, forecast_url):
    try:
        
        response = requests.get(current_weather_url.format(city,apikey)).json()
        lat= response['coord']['lat']
        lon =response['coord']['lon']
        print(response)
    
        ####=========== Filling in the lat AND lon place holders ========#####
        forecast_response = requests.get(forecast_url.format(lat, lon, apikey)).json()
        print('forecast_response= ', forecast_response,forecast_url,apikey)
    
        
    except  KeyError as e:
        return  {"error":"Invalid City Name"}
        #raise  Exception ("API returned unexpected data structure.") from e
        
       # messages.error(request,"The city your Entered can not be Accessed")
        #return render(request, 'index.html') 
    weather_data = {
        "city": city,
        "temperature": round(response['main']['temp'] - 273.15, 2),
        "description": response['weather'][0]['description'],
        "icon": response['weather'][0]['icon']
    }
    
    daily_forecasts = []
    
    for daily_data in forecast_response['daily'][:5]:
        daily_forecasts.append({
            "day":datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A"),
            "min_temp": round(daily_data['temp']['min'] - 273.15, 2),
            "max_temp": round(daily_data['temp']['max'] - 273.15, 2),
            "description": daily_data['weather'][0]['description'],
            "summary": daily_data['summary'],
            "icon": daily_data['weather'][0]['icon'],
        })
    return weather_data, daily_forecasts

    

