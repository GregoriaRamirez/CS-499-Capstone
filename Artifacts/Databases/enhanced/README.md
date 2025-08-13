# Databases — Enhanced Artifact

## Description

This enhanced artifact contains the refactored database integration for the Animal Shelter Dashboard, focusing on **Database** improvements. The MongoDB URI is now stored securely in a `.env` file and loaded using `python-dotenv`, eliminating hardcoded credentials.

A dedicated `AnimalShelter` class was created to handle all `CRUD` (create, read, update and delete) operations, keeping database logic separate from UI and filtering code. Structured error handling was added to catch connection issues early, and logging was implemented to monitor database activity.

These changes improved security, maintainability, and readiness for real-world deployment.


## Key Enhancements
- **Secure Connection:** Credentials stored in `.env` file and loaded using `python-dotenv`.
- **Error Handling:** Try/except blocks to prevent crashes if the database is unreachable.
- **Logging:** Structured logging for database operations.
- **Connection Cleanup:** Ensures MongoDB client is closed after operations.
- **Data Cleaning:** Converts MongoDB output to a Pandas DataFrame and removes the `_id` field.

## Benefits
The project now follows professional security practices and is more reliable for production use.

