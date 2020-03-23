#! python3
#Print the weather 

import json, requests, sys

if len(sys.argv) < 2:
    print('Usage: weather_printer.py location')
    sys.exit()
location = ''.join(sys.argv[1:])

print(location)

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=bc83d48c836d490942ba3511ebca51de'.format(location)

response = requests.get(url)
weather_data = json.loads(response.text)

print('The current weather in {}.'.format(location))
print('------------------------------')
print('General description: {}'.format(weather_data['weather'][0]['description']))