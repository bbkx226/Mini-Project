import requests

API_KEY = "5569264d77d68aa18a308791b2fa067c"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data["main"]["temp"]
    temp = temperature - 273.15
    print(data['wind']['speed'])
    print(f"Weather: {weather} \nTemperature: {round(temp, 2)} celsius")
else:
    print("An error occured. ")

print(data)