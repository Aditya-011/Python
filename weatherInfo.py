import requests
import json
city = input("Enter A City : ")
api_key = "d72851ccd0eb4bfa12417d601a585b8f"
base_url = "https://api.openweathermap.org/data/2.5/weather?"
url = base_url + "appid=" + api_key+"&units=metric" + "&q=" + city
response = requests.get(url)
x = response.json()
#print(x)
if x['cod'] == 200:
    print("City Name : ", x['name'])
    print("Weather : ", x['weather'])
    print("Weather : ", x['weather'][0]['main'])
    print("Temp : ", x['main']['temp'],"C")
    print("Minimum Temp : ", x['main']['temp_min'],"C")
    print("Max Temp : ", x['main']['temp_max'],"C")
else:
    print("City Not Found")
