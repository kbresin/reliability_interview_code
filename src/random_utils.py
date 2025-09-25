import requests
import re

# this class is used by get_weather function below
# no need to write unit tests for this specific class
# weatherstack.com is a real site
# when writing your unit test for get_weather please assume that your tests run
# in an environment where you lack access to a valid API key for weatherstack.co
class WeatherRetriever:

    def __init__(self, api_key: str):
        self.api_key = api_key

    def city_current_weather(self, city: str):
        url = f"https://api.weatherstack.com/current?access_key={self.api_key}&query={city}"
        response = requests.get(url)
        return response.json()


class RandomUtils:

    def __init__(self):
        pass

    def is_palindrome(self, s: str):
        clean_s = ''.join(char.lower() for char in s if char.isalnum())
        return clean_s == clean_s[::-1]

    # calculate_discount(10, 0.1) -> 9.0
    def calculate_discount(self, base_price: float, discount_percent: float) -> float:
        return base_price - base_price * discount_percent

    def is_valid_email(self, email: str) -> bool:
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None

    def get_weather(self, city: str):
        weather_retriever = WeatherRetriever(api_key="YOUR_API_KEY")
        weather_data = weather_retriever.city_current_weather(city)

        location = weather_data['city']['name']
        time = weather_data['current']['observation_time']
        temperature = weather_data['current']['temperature']
        formatted_message = f"The weather in {location} is {temperature} degrees Celsius at {time}"
        return formatted_message
