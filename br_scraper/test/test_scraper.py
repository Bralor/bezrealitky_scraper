import pytest

from br_scraper.src.scraper import Scraper


class TestScraper:
    def setup(self):
        url = "https://www.bezrealitky.cz/api/record/markers"
        self.test = Scraper(url, "br_scraper/data", "prostejov")

    def test_find_params_is_str(self):
        assert isinstance(self.test.find_params(), str)

    def test_find_params(self):
        assert self.test.find_params()

    def test_get_module_path(self):
        assert self.test.get_module_name("prostejov.py")[0] \
            == "br_scraper/data/prostejov.py"

    def test_get_module_name(self):
        assert self.test.get_module_name("prostejov.py")[1] \
            == "br_scraper.data.prostejov"

    def test_get_incorrect_path(self):
        assert self.test.get_module_name("prostejov")[0] \
            != "br_scraper/data/prostejov.py"

    def test_get_incorrect_name(self):
        assert self.test.get_module_name("prostejov")[1] \
            != "br_scraper.data.prostejov"

    def test_cannot_load_params(self):
        with pytest.raises(Exception):
            self.test.load_params("kromeriz")

    def test_load_params_with_no_param(self):
        with pytest.raises(Exception):
            self.test.load_params()

    def test_load_params_output_type(self):
        assert isinstance(self.test.load_params(
            "br_scraper/data/prostejov.py",
            "br_scraper.data.prostejov"
        ), dict)

    def test_load_params_output_keys(self):
        assert \
            self.test.load_params(
                "br_scraper/data/prostejov.py",
                "br_scraper.data.prostejov"
            ).get("offerType") == "prodej"

    def test_cannot_find_params(self):
        with pytest.raises(Exception):
            self.test.find_params("data")

    def test_missing_params(self):
        with pytest.raises(Exception):
            self.test.send_request()

    def test_read_json(self):
        file = '[{"id":"671048"}]'
        json = self.test.read_json(file)
        assert json == [{'id': '671048'}]

    def test_cannot_read_json(self):
        file = [{"id":"671048"}]
        with pytest.raises(Exception):
            self.test.read_json(file)


