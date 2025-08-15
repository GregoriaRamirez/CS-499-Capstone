from pymongo import MongoClient
from bson.objectid import ObjectId

class DatabaseError(Exception):
    """Custom exception for database errors."""
    pass

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
        try:
            self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
            self.database = self.client[DB]
            self.collection = self.database[COL]
            print("Connected to MongoDB")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            raise DatabaseError(f"Failed to connect to database: {e}")

    def close(self):
        """Close the MongoDB connection"""
        self.client.close()
        print("MongoDB connection closed.")

    def create(self, data):
        """Inserts a document into the database"""
        if data and isinstance(data, dict):
            try:
                result = self.collection.insert_one(data)
                return bool(result.inserted_id)
            except Exception as e:
                raise DatabaseError(f"Error inserting data: {e}")
        else:
            raise ValueError("Invalid data: must be a non-empty dictionary")

    def read(self, query={}):
        """Queries documents from the database"""
        if isinstance(query, dict):
            try:
                result = list(self.collection.find(query))
                # Convert ObjectId to string to prevent errors in JSON serialization
                for document in result:
                    document['_id'] = str(document['_id'])  # Convert ObjectId to string
                return result if result else []  # Return empty list if no results
            except Exception as e:
                raise DatabaseError(f"Error reading from database: {e}")
        else:
            raise ValueError("Invalid query: must be a dictionary")

    def update(self, query, update_data, multiple=False):
        """Updates document(s) in the database"""
        if not isinstance(query, dict) or not isinstance(update_data, dict):
            raise ValueError("Both query and update_data must be dictionaries.")
        
        try:
            if multiple:
                result = self.collection.update_many(query, {'$set': update_data})
            else:
                result = self.collection.update_one(query, {'$set': update_data})
            return result.modified_count
        except Exception as e:
            raise DatabaseError(f"Error updating database: {e}")

    def delete(self, query, multiple=False):
        """Deletes document(s) from the database"""
        if not isinstance(query, dict):
            raise ValueError("Query must be a dictionary.")
        
        try:
            if multiple:
                result = self.collection.delete_many(query)
            else:
                result = self.collection.delete_one(query)
            return result.deleted_count
        except Exception as e:
            raise DatabaseError(f"Error deleting from database: {e}")

  
