import unittest
from unittest.mock import patch
from LastFM import LastFM


class TestLastFM(unittest.TestCase):
    def setUp(self):
        self.lastfm = LastFM(user='joynts')
        self.lastfm.set_apikey('17174252eee13cd769ba767b9f5c8963')
