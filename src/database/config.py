from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class DBConfig:
    def __init__(self):
        self.db_client = None
        self.payments_management_db = None
        self.todos_collection = None
        self.payments_collection = None

    def get_db_client(self):
        if not self.db_client:
            uri = "mongodb+srv://manuellanouko:Ns29kWUPALeRYqBC@mn-mogo-cluster.dmekj.mongodb.net/?retryWrites=true&w=majority&appName=mn-mogo-cluster"
            self.db_client = MongoClient(uri, server_api=ServerApi('1'))
        return self.db_client

    def get_payments_management_db(self):
        if not self.payments_management_db:
            self.payments_management_db = self.get_db_client().payments_management_db
        return self.payments_management_db

    def get_payments_collection(self):
        if not self.payments_collection:
            self.payments_collection = self.get_payments_management_db()["payment"]
        return self.payments_collection

    def get_todos_collection(self):
        if not self.todos_collection:
            self.todos_collection = self.get_payments_management_db()["todo"]
        return self.todos_collection
