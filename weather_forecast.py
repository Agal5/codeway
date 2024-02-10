import requests 
import json 

print("WHEATHER FORECASTER")
api_key="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/india?unitGroup=us&key=YOUR_API_KEY&contentType=json"
base_url="https://api.openweathermap.org/data/2.5/weather"
city = input("Enter City : ")
complete_url=base_url+"?appid="+api_key+"&q="+city

response = requests.get(complete_url)
data = response.json()

if data["cod"]!="404":
    main = data["main"]
    temp = main["temp"]
    pressure = main["pressure"]
    humidity = main["humidity"]
    weather = data["weather"]
    description = weather[0]["description"]
    
    print("Temperature (in kelvin):" +str(temp))
    print("Atmosphere (in hPa unit):" +str(pressure))
    print("Humidity (in %):"  +str(humidity))
    print("Description :" +description)
else:
    print("City not found")    
    