import os
from dotenv import load_dotenv
from pymongo import MongoClient
import pandas as pd
import logging

# Enhancement (Software Design): Use environment variables and logging instead of hardcoded values and print

# Load environment variables from example.env
load_dotenv("example.env")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_data():
    try:
        # Use environment variables for MongoDB connection
        user = os.getenv("MONGO_USER")
        password = os.getenv("MONGO_PASS")
        host = os.getenv("MONGO_HOST")
        port = int(os.getenv("MONGO_PORT"))
        db_name = os.getenv("MONGO_DB")
        collection_name = os.getenv("MONGO_COL")

        # Build URI conditionally depending on whether credentials exist
        if user and password:
            uri = f"mongodb://{user}:{password}@{host}:{port}/"
        else:
            uri = f"mongodb://{host}:{port}/"

        client = MongoClient(uri)
        db = client[db_name]
        collection = db[collection_name]

        mongo_data = list(collection.find())
        df = pd.DataFrame(mongo_data)

        if '_id' in df.columns:
            df.drop(columns=['_id'], inplace=True)

        logger.info("MongoDB data successfully retrieved.")
        return df

    except Exception as e:
        logger.error(f"Error retrieving data: {e}")
        return pd.DataFrame()
