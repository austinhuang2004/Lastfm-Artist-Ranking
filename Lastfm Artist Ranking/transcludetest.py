from WebAPI import WebAPI
from OpenWeather import OpenWeather
from LastFM import LastFM


def test_api(message: str, apikey: str, webapi: WebAPI):
  webapi.set_apikey(apikey)
  webapi.load_data()
  result = webapi.transclude(message)
  print(result)


open_weather = OpenWeather()    # notice there are no params here...HINT: be sure to use parameter defaults!!!
lastfm = LastFM()

test_api("Testing the weather: @weather", '0d7931bceeb0bd810702e133c92e1a84', open_weather)
# expected output should include the original message transcluded with the default weather value for the @weather keyword.

test_api("Testing lastFM: @lastfm", '0ec0459675b353e6dd27dbe2d55f0404', lastfm)
# expected output include the original message transcluded with the default music data assigned to the @lastfm keyword
