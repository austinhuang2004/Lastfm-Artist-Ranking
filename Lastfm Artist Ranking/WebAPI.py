# webapi.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Austin Huang
# austh10@uci.edu
# 28821105
import json
import urllib
import urllib.error
import urllib.request
from abc import ABC, abstractmethod


class WebAPI(ABC):
    '''
    This is the abstract class for the web API
    '''
    def _download_url(self, url: str) -> dict:
        '''
        Downloads and returns the URL into JSON format.
        Also includes error handling.
        '''
        try:
            response = urllib.request.urlopen(url)
            json_results = response.read()
            weather_data = json.loads(json_results)
            return weather_data
        except urllib.error.HTTPError as error:
            if error.code == 404:
                print("The remote API is unavailable because of invalid zip/country code")
            elif error.code == 503:
                print("The remote API is unavailable since it cannot handle the request")
            else:
                print('Failed to download contents of URL')
                print(f'Status code: {error.code}')
            raise error
        except urllib.error.URLError as error:
            print(f'This URL failed because it could not download the contents of {error.reason}')
            raise error
        except json.JSONDecodeError as error:
            print(f'This API has failed because it could not parse the reponse of {error.msg}')
            raise error

    def set_apikey(self, apikey: str) -> None:
        '''
        API key for the web API.
        '''

    @abstractmethod
    def load_data(self):
        '''
        Abstract method to load the data from web API.
        '''

    @abstractmethod
    def transclude(self, message: str) -> str:
        '''
        Abstract method to transclude the message from the API data
        '''
