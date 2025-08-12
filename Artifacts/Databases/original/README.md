# Databases — Original Artifact

## Description
The original database connection code was embedded directly in the main application, using hardcoded credentials and no error handling.

## Limitations
- Hardcoded MongoDB credentials in the code.
- No connection error handling — application would crash if DB was unavailable.
- Database logic mixed with UI code.
- No logging or cleanup of database connections.

## Technologies Used
- Python
- MongoDB
- PyMongo
