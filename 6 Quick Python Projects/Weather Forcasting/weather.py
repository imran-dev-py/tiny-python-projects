import requests

def weather_info(city_name):
	# https://openweathermap.org/current
	API_KEY='195aa1c32f356ea71fefaea1547ee89c'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	base_url = f'{url}?q={city_name}&appid={API_KEY}'
	response = requests.get(base_url).json()

	# Country
	print(f"Country Code is `{response['sys']['country']}`")

	# Current Temperature in celsius
	kelvin = response['main']['temp']
	celsius = (kelvin - 273.15)
	print(f'Today\'s Weather is {celsius:.2f}°C')

	# Sky Description
	print(f"Sky is `{response['weather'][0]['description']}`")

city_name = input('Provide City name to see the current weather info: ')
weather_info(city_name)