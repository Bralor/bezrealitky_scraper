import sys

from br_scraper.src.scraper import Scraper
from br_scraper.src.parser import Parser
from br_scraper.src.db import DbWrapper


def scraper(basename: str, location: str):
    offers = []

    scrape = Scraper(basename, "br_scraper/data", location)
    file = scrape.find_params()
    path, module = scrape.get_module_name(file)
    params = scrape.load_params(path, module)
    scrape.send_request(params)
    results = scrape.read_json(scrape.response)

    for result in results:
        parser = Parser(basename, result)
        parsed_dict = parser.parse_details(parser.collection)
        offers.append(parsed_dict)

    insert_offers = DbWrapper("localhost", 27017, "br_data", "offers", offers)
    insert_offers.connect_db()
    insert_offers.add_indexing("auction_id")
    insert_offers.write_documents(offers)


def main():
    basename = "https://www.bezrealitky.cz/api/record/markers"
    location = sys.argv[1]
    scraper(basename, location)


if __name__ == "__main__":
    main()

