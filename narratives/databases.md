---
layout: default
title: Databases Enhancement
permalink: /artifact-databases
---

**Navigation:**  
[🏠 Home](index.md) | [📝 Self-Assessment](self-assessment.md) | [🙋‍♀️ About Me](about.md) | [📂 Projects](projects.md) | [🛠️ Software Design](artifact-software.md) | [🧠 Algorithms](artifact-algorithms.md) | [💾 Databases](artifact-databases.md) | [🏆 Awards](awards.md) | [📄 Résumé](resume.md)

# 💾 Databases Artifact

## 📌 Artifact Description
For the databases category, I selected the backend database connection and retrieval code from my Animal Shelter Dashboard project. This project was originally built in CS 340: Client-Server Development using Jupyter Notebook with direct Mongo shell commands and hardcoded credentials.  

For my CS 499 Capstone, I enhanced this component to make database access more secure, modular, and production-ready. The changes include secure credential management with `.env` files, structured logging, error handling, and automatic conversion of MongoDB documents into a pandas DataFrame for dashboard use.

---

## 📎 Justification for Inclusion
I chose this artifact because it demonstrates my ability to improve database interaction security, maintainability, and efficiency. The original version used a class with hardcoded credentials and no separation of database logic from the rest of the app. The enhanced version follows professional best practices for NoSQL database integration, ensuring a clean architecture and safer deployment.

---

## 📝 Examples Before and After Enhancements

**Original Code (Before Enhancement):**
```python
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
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
```

**Issues in Original Version:**
1. Hardcoded credentials expose sensitive information.
2. No error handling for failed connections.
3. All logic mixed inside a single class, making reuse harder.
4. No structured logging for monitoring.
5. Returned raw MongoDB results instead of a clean DataFrame.

---

**Enhanced Code (After Enhancement):**
```python
import os
import pandas as pd
import logging
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_data():
    client = None
    try:
        user = os.getenv("MONGO_USER")
        password = os.getenv("MONGO_PASS")
        host = os.getenv("MONGO_HOST", "localhost")
        port = int(os.getenv("MONGO_PORT", 27017))
        db_name = os.getenv("MONGO_DB")
        collection_name = os.getenv("MONGO_COL")

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

    finally:
        if client:
            client.close()
```

---

## 🔑 Key Enhancements
1. **Secure Credential Management** – Moved username, password, host, and database details into a `.env` file loaded with `python-dotenv`.
2. **Modular Function Design** – Replaced the embedded connection in a class with a reusable `get_data()` function that can be imported anywhere in the app.
3. **Structured Logging** – Added `logging` instead of print statements to allow better debugging and monitoring.
4. **Error Handling** – Wrapped MongoDB connection in try/except with clear error messages and a safe fallback to an empty DataFrame.
5. **Automatic DataFrame Conversion** – Converted MongoDB documents directly to a pandas DataFrame and dropped the `_id` column for cleaner dashboards.
6. **Connection Safety** – Ensured the MongoDB client closes after each operation to prevent resource leaks.

---

## 🎯 Alignment to Program Outcomes
- **Outcome 4:** Implemented a computing solution using proper tools and industry practices by applying `.env` files, logging, and structured connection handling.
- **Outcome 5:** Demonstrated a security mindset by removing hardcoded credentials, limiting exposure of sensitive information, and handling database errors gracefully.

---

## 🔍 Reflection
Enhancing this artifact taught me the value of treating the database layer as a separate, secure, and modular part of the application.  
One challenge was making the `get_data()` function flexible enough to work in different environments without changing the code. Another was ensuring that the dashboard still functioned correctly when no database connection was available — something the original code could not handle.

This enhancement made the project more secure, maintainable, and ready for real-world deployment, and it reflects my growth in professional database integration for Python applications.

---

