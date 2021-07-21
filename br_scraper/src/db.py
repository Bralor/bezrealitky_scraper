import pymongo


class DbWrapper():
    def __init__(self, hostname: str, port: int, db_name: str,
                 col_name: str, data: list) -> None:
        self.hostname = hostname
        self.port = port
        self.db_name = db_name
        self.col_name = col_name

        if not data:
            raise Exception("There are no data to insert")
        else:
            self.data = data


    def connect_db(self) -> None:
        try:
            self.client = pymongo.MongoClient(
                self.hostname,
                self.port
            )

        except pymongo.errors.ServerSelectionTimeoutError as err:
            raise Exception(f"Cannot connect to the db ({err})")
        else:
            if not self.db_exists() and not self.col_exists():
                self.create_collection()
            else:
                self.db = self.client[self.db_name]
                self.collection = self.db[self.col_name]
                print("Using existing database and collection")


    def db_exists(self) -> bool:
        return self.db_name in self.client.list_database_names()


    def col_exists(self) -> bool:
        return self.col_name in self.client[self.db_name].list_collection_names()


    def create_collection(self) -> None:
        self.db = self.client[self.db_name]
        self.collection = self.db[self.col_name]
        print(f"Collection {self.col_name} created")


    def add_indexing(self, index_name: str) -> None:
        self.collection.create_index(
            [(index_name, pymongo.ASCENDING)],
            unique=True
        )

    def write_documents(self, data: list) -> None:
        if not data and not isinstance(data, list):
            raise Exception("Argument 'data' is not list or is empty")

        self.collection.insert_many(data)


    def read_documents(self) -> list:
        if not self.collection:
            raise Exception("Argument 'collection' is empty")

        return [
            document
            for document in self.collection.find({})
        ]

