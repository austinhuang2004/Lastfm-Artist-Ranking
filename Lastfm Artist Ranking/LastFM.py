'''
Module Docstring: This module defines the class LastFM to retrive data from the lastfm web API. 
'''

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Austin Huang
# austh10@uci.edu
# 28821105

# key: 17174252eee13cd769ba767b9f5c8963
# shared secret: 2a91345ebd6c753adb8ab4df5726900e
from WebAPI import WebAPI


class LastFM(WebAPI):
    '''
    Class Docstring: This class provides
    the functionality to get and receive the data from the lastfm web API
    '''
    def __init__(self, user: str = 'joynts') -> None:
        '''
        Makes a new instance for the lasfm class.
        '''
        self.apikey = None
        self.user = user
        self.artist = None

    def set_apikey(self, apikey: str) -> None:
        '''
        Sets the API key to be used for calling.
        '''
        self.apikey = apikey

    def load_data(self) -> None:
        '''
        Gets the artist data from the lastfm API.
        '''
        url = f"http://ws.audioscrobbler.com/2.0/?method=library.getartists&api_key={self.apikey}&user={self.user}&format=json"
        artists_info = self
        artists_info = artists_info._download_url(url)
        self.artist = artists_info['artists']['artist'][0]['name']

    def transclude(self, message: str) -> str:
        '''
        Replaces the keyword in order to return the transcluded message.
        '''
        if '@lastfm' in message:
            return message.replace('@lastfm', self.user)
        return message
