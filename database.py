import pymongo
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

load_dotenv()

class MongoDB:

    def __init__(self):
        # Load env values
        db_name = os.getenv("DB_NAME")
        username = quote_plus(os.getenv("DB_USER"))
        password = quote_plus(os.getenv("DB_PASSWORD"))

        # Connection URL (cluster kept in code, as you requested)
        connection_url = (
            f"mongodb+srv://{username}:{password}"
            "@gemini-bot-0.mv8vq6l.mongodb.net/"
            "?retryWrites=true&w=majority&appName=gemini-bot-0"
        )

        # Connect to MongoDB
        self.client = pymongo.MongoClient(connection_url)
        self.db = self.client[db_name]

        # Collections (you may use them later)
        self.users_collection = self.db["users"]
        self.sentiment_logs_collection = self.db["sentiment_logs"]
        self.translations_collection = self.db["translations"]

    # ---------- USERS CRUD ----------

    def insert_user(self, data):
        return self.users_collection.insert_one(data)

    def find_user(self, query):
        return self.users_collection.find_one(query)

    def find_all_users(self):
        return list(self.users_collection.find())

    # ---------- SENTIMENT LOGS CRUD ----------

    def insert_sentiment_log(self, data):
        return self.sentiment_logs_collection.insert_one(data)

    def find_sentiment_log(self, query):
        return self.sentiment_logs_collection.find_one(query)

    def find_all_sentiment_logs(self):
        return list(self.sentiment_logs_collection.find())

    # ---------- TRANSLATIONS CRUD ----------

    def insert_translation(self, data):
        return self.translations_collection.insert_one(data)

    def find_translation(self, query):
        return self.translations_collection.find_one(query)

    def find_all_translations(self):
        return list(self.translations_collection.find())