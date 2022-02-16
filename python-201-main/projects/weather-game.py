# Include the current weather into your game mechanics.
import requests
from pprint import pprint

city=input("From which city are you playing? The game will look like it today! ")
if " " in city:
    a=city.split()
    ciudad=a[0]+"%20"+a[1]
else:
    ciudad=city

URL = "https://www.metaweather.com/api/location/search/?query="+ciudad
request=requests.get(URL).json()
woeid=request[0]["woeid"]

url2="https://www.metaweather.com/api/location/"+str(woeid)
weather=requests.get(url2).json()["consolidated_weather"][0]["weather_state_name"]
temp=requests.get(url2).json()["consolidated_weather"][0]["the_temp"]
humidity=requests.get(url2).json()["consolidated_weather"][0]["humidity"]
visibility=requests.get(url2).json()["consolidated_weather"][0]["visibility"]
print(f"The weather in {city} is {weather} with a temperature of {temp}. Be aware! that humidity will be {humidity} and use it in your favor, that the visibility will be {visibility}")

