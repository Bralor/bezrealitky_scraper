import pytest

from br_scraper.src.parser import Parser
from br_scraper.src.flatten import flattenDict


class TestParser:
    def setup(self):
        testing_basename = "https://foobar.com/"
        testing_dict = {
            'id': 'XXX',
            'uri': 'XXX',
            'keyAdvertType': 'XXX',
            'type': '',
            'timeOrder': {
                'date': '2021-06-25 22:50:02.000000',
                'timezone_type': 3,
                'timezone': 'Europe/Berlin'
            },
            'orderPriority': 0,
            'advertEstateOffer': [
                {
                    'gps': '{"lat":XX.XXXX,"lng":XX.XXXXX}',
                    'price': 1000000,
                    'currency': 'CZK',
                    'keyOfferType': 'XXX',
                    'keyEstateType': 'XXX',
                    'keyDisposition': 'XXX',
                    'surface': 74,
                    'surfaceLand': 0,
                    'id': 'XXX'
                }
            ]
        }
        self.test = Parser(testing_basename, testing_dict)

    def test_input_correct_object(self):
        assert isinstance(self.test.is_dict({"foo": "bar"}), bool)

    def test_input_incorrect_object(self):
        with pytest.raises(Exception):
            self.test.is_dict(["foo", "bar"])

    def test_has_correct_keys(self):
        mandatory_keys = [
            "id", "uri",
            "advertEstateOffer.gps0",
            "advertEstateOffer.price0",
            "advertEstateOffer.currency0",
            "advertEstateOffer.surface0",
            "advertEstateOffer.keyDisposition0",
            "advertEstateOffer.keyEstateType0"
        ]

        for key in mandatory_keys:
            assert key in flattenDict(self.test.collection)

    def test_has_incorrect_keys(self):
        assert "price" not in flattenDict(self.test.collection)

