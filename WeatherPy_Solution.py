### WeatherPy ###
from citipy import citipy
import requests
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time



# api keys
api_key = "a08d21f17a96425969576de80711a620"

# target url
#name = ''
#target_url = "api.openweathermap.org/data/2.5/weather?q=" + name
weather = []
request_count = 0
#city_weather = requests.get(target_url).json()

# generate random coordinate pairs
# Create random indices representing, for instance, a user's choice of posts
#indices = random.sample(list(range(1, 100)), 10)


#
coordinates = [(200, 200), (23, 200), (42, 100)]
cities = []
temperatures = []

for coordinate_pair in coordinates:
    lat, lon = coordinate_pair
    cities.append(citipy.nearest_city(lat, lon))

for city in cities:
    name = city.city_name
    target_url = "http://api.openweathermap.org/data/2.5/forecast?q=%s1&APPID={%s}" % (
        name, api_key)
    city_weather = requests.get(target_url).json()
    request_count += 1
    print(request_count)
    print(name)
    print(target_url)
    print(city_weather)


# Plot the temperatures over time
plt.plot(lat, temps)
#formatter = DateFormatter('%Y-%m-%d %H:%M:%S')
plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
plt.gcf().autofmt_xdate()
plt.show()

# Temperature (F) vs. Latitude
# Humidity (%) vs. Latitude
# Cloudiness (%) vs. Latitude
# Wind Speed (mph) vs. Latitude
