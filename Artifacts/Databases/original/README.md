# Databases — Original Artifact

## Description

This original artifact contains the database integration for the Animal Shelter Dashboard, developed during CS 340: Client-Server Development. The MongoDB connection string was hardcoded directly into the script, posing a security risk.  

Database operations, create, read, update and delet (CRUD), were written directly into the main application logic, with no separation of responsibilities. Error handling was minimal, and there was no logging to track database issues.  

This version serves as the baseline for comparing later enhancements that introduced secure credential handling, dedicated database classes, and structured error handling.

## Limitations
- Hardcoded MongoDB credentials in the code.
- No connection error handling — application would crash if DB was unavailable.
- Database logic mixed with UI code.
- No logging or cleanup of database connections.

## Technologies Used
- Python
- MongoDB
- PyMongo
