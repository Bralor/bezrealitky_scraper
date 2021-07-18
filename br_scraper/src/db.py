import pymongo


class DbWrapper():
    def __init__(self, host: str, port: str, db_name: str, col: str, data: list) -> None:
        self.host = host
        self.port = port
        self.db_name = db_name
        self.col = col

        if not data:
            raise Exception("There are no data to insert")
        else:
            self.data = data


    def connect_db(self) -> None:
        try:
            self.client = pymongo.MongoClient(self.host, self.port)

        except pymongo.errors.ServerSelectionTimeoutError as err:
            raise Exception(f"Cannot connect to the db ({err})")
        else:
            if not self.db_exists():
                self.create_collection()
                print(f"Collection {self.col} already exists")
            else:
                self.db = self.client[self.db_name]


    def db_exists(self) -> bool:
        return self.db_name in self.client.list_database_names()


    def create_collection(self) -> None:
        self.db = self.client[self.db_name]
        self.collection = self.db[self.col]
        print(f"Collection {self.col} created")


    def write_documents(self, data: list) -> None:
        if not data:
            raise Exception("Data object is empty")

        # missing indexing
        for item in data:
            self.db[self.db_name].insert_one(item)
