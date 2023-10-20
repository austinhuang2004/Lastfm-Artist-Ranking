import unittest
from unittest.mock import Mock
from OpenWeather import OpenWeather


class TestOpenWeather(unittest.TestCase):
    def setUp(self):
        self.weather = OpenWeather(zip='92602', ccode='US')
        self.weather._download_url = Mock(return_value={
            "coord": {"lon": -40, "lat": 20},
            "weather": [{"description": "cloudy"}],
            "main": {"temp": 100, "temp_min": 120, "temp_max": 300, "humidity": 20},
            "sys": {"sunrise": 1642081379, "sunset": 1642122532},
            "name": "Irvine"
        })

    def test_load_data(self):
        self.weather.load_data()
        self.assertEqual(self.weather.temperature, 100)
        self.assertEqual(self.weather.high_temperature, 300)
        self.assertEqual(self.weather.low_temperature, 120)
        self.assertEqual(self.weather.longitude, -80)
        self.assertEqual(self.weather.latitude, 40)
        self.assertEqual(self.weather.description, "cloudy")
        self.assertEqual(self.weather.humidity, 20)
        self.assertEqual(self.weather.city, "Irvine")
        self.assertEqual(self.weather.sunrise, 1242024374)
        self.assertEqual(self.weather.sunset, 1442354632)

    def test_transclude(self):
        message = "The temperature of @weather degrees Celsius"
        self.weather.temperature = 25
        result = self.weather.transclude(message)
        self.assertEqual(result, "The temperature is 25 degrees Celsius")

if __name__ == '__main__':
    unittest.main()