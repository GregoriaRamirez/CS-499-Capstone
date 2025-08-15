
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self):
        # MongoDB Connection Variables
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32440
        DB = 'AAC'
        COL = 'animals'
        
        # Initialize MongoDB Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """Inserts a document into the database"""
        if data and isinstance(data, dict):
            result = self.collection.insert_one(data)
            return bool(result.inserted_id)
        else:
            raise ValueError("Invalid data: must be a non-empty dictionary")

    def read(self, query={}):
        """Queries documents from the database"""
        print(f"Query type: {type(query)}")  # Log query type
        print(f"Query: {query}")  # Log the query
        if isinstance(query, dict):
            result = list(self.collection.find(query))
            return result if result else []
        else:
            raise ValueError("Invalid query: must be a dictionary")
        
    def update(self, query, update_data, multiple=False):
        """Updates document(s) in the database
        
        Args:
            query (dict): The query to find the document(s) to update.
            update_data (dict): The key-value pairs to update.
            multiple (bool): If True, updates all matching documents. If False, updates one document.
        
        Returns:
            int: The number of documents modified.
        """
        if not isinstance(query, dict) or not isinstance(update_data, dict):
            raise ValueError("Both query and update_data must be dictionaries.")
        
        if multiple:
            result = self.collection.update_many(query, {'$set': update_data})
        else:
            result = self.collection.update_one(query, {'$set': update_data})
        
        return result.modified_count

    def delete(self, query, multiple=False):
        """Deletes document(s) from the database.
        
        Args:
            query (dict): The query to find the document(s) to delete.
            multiple (bool): If True, deletes all matching documents. If False, deletes one document.
        
        Returns:
            int: The number of documents deleted.
        """
        if not isinstance(query, dict):
            raise ValueError("Query must be a dictionary.")
        
        if multiple:
            result = self.collection.delete_many(query)
        else:
            result = self.collection.delete_one(query)
        
        return result.deleted_count

    def read(self, query):
        """Queries documents from the database"""
        if query and isinstance(query, dict):
            result = list(self.collection.find(query))
            return result if result else []
        else:
            raise ValueError("Invalid query: must be a dictionary")
