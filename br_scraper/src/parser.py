class Parser:
    def __init__(self, basename: str, collection: dict) -> None:
        self.basename = basename
        self.collection = collection

    @staticmethod
    def is_dict(col: dict) -> bool:
        if not isinstance(col, dict):
            raise Exception("Data type 'collection' is not dictionary")
        return True

    def parse_details(self, data: dict):
        if self.is_dict(data):
            return {
                "auction_id": f"{data['id']}",
                "name": f"{data['uri'].split('-', maxsplit=1)[1]}",
                "price": data["advertEstateOffer"][0]["price"],
                "currency": data["advertEstateOffer"][0]["currency"],
                "surface": data["advertEstateOffer"][0]["surface"],
                "url": f"{self.basename}{data['uri']}",
                "gps": data["advertEstateOffer"][0]["gps"],
                "disposition": data["advertEstateOffer"][0]["keyDisposition"],
                "estate_type": data["advertEstateOffer"][0]["keyEstateType"]
            }

