import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
WS_URL = "http://api.weatherstack.com/current"

cities = []
with open("cities.txt") as f:
    for line in f:
        cities.append(line.strip())

print("Cities to fetch weather for:", cities)

for city in cities:
    parameters = {'access_key': API_KEY, 'query': city}
    response = requests.get(WS_URL, params=parameters)
    js = response.json()
    
    if 'current' in js and 'location' in js:
        temperature = js['current']['temperature']
        date = js['location']['localtime']
        with open(f"{city}.txt", "a") as f:
            f.write(f"{date},{temperature}\n")
    else:
        print(f"Error fetching data for {city}: {js.get('error', 'Unknown error')}")

print('Done!')
