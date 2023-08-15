from pymongo import MongoClient
from configs.load_config import get_configs


class MongoDBConnector:
    def __init__(self, host, port, database, collection):
        self.host = host
        self.port = port
        self.database = database
        self.collection = collection
        self.client = None

    def connect(self):
        self.client = MongoClient(self.host, self.port)
        self.db = self.client[self.database]
        self.coll = self.db[self.collection]
        print("Connected to MongoDB")

    def disconnect(self):
        if self.client:
            self.client.close()
            print("Disconnected from MongoDB")

    def query_data(self, query):
        results = self.coll.find(query)
        return list(results)

    def insert_data(self, data):
        result = self.coll.insert_one(data)
        print("Data inserted. ID:", result.inserted_id)

    def update_data(self, query, update):
        result = self.coll.update_many(query, update)
        print("Data updated. Matched documents:", result.matched_count)

    def delete_data(self, query):
        result = self.coll.delete_many(query)
        print("Data deleted. Deleted documents:", result.deleted_count)


configs = get_configs()
connector = MongoDBConnector(configs["mongodb"]["host"], configs["mongodb"]
                             ["port"], configs["mongodb"]["database"], connection)
connector.connect()
