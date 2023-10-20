'''
Module Docstring: This module defines the class openweather 
and retrieves data from the openweather web API.
'''
# openweather.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Austin Huang
# austh10@uci.edu
# 28821105

# key = 0d7931bceeb0bd810702e133c92e1a84

from WebAPI import WebAPI


class OpenWeather(WebAPI):
    '''This class retrieves data from the OpenWeather API'''
    def __init__(self, zip: str = '92602', ccode: str = 'US') -> None:
        '''
        Making the self for the different things that need to be indexed
        '''
        self.zip = zip
        self.ccode = ccode
        self.humidity = None
        self.sunrise = None
        self.apikey = None
        self.temperature = None
        self.high_temperature = None
        self.low_temperature = None
        self.longitude = None
        self.latitude = None
        self.description = None
        self.city = None
        self.sunset = None
        self.keywords = ["@weather"]

    def set_apikey(self, apikey: str) -> None:
        '''
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service
        '''
        self.apikey = apikey

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and store the response in class data attributes.
        '''
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zip},{self.ccode}&appid={self.apikey}"
        weather_data = self
        weather_data = weather_data._download_url(url)
        self.temperature = weather_data["main"]["temp"]
        self.high_temperature = weather_data["main"]["temp_max"]
        self.low_temperature = weather_data["main"]["temp_min"]
        self.longitude = weather_data["coord"]["lon"]
        self.latitude = weather_data["coord"]["lat"]
        self.description = weather_data["weather"][0]["description"]
        self.humidity = weather_data["main"]["humidity"]
        self.city = weather_data["name"]
        self.sunrise = weather_data["sys"]["sunrise"]
        self.sunset = weather_data["sys"]["sunset"]

    def transclude(self, message: str) -> str:
        '''
        Replaces the keyword in order to return the transcluded message
        '''
        if '@weather' in message:
            return message.replace('@weather', str(self.temperature))
        return message
