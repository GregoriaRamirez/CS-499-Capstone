# Software Design & Engineering — Original Artifact

This original artifact contains the Animal Shelter Dashboard code in its initial form, developed during CS 340: Client-Server Development. At this stage, the code was written in a single Jupyter Notebook without a clear modular structure. Backend logic, user interface elements, and database operations were combined in the same file, making the project harder to maintain and scale.

The database connection string (MongoDB URI) was hardcoded directly in the script using school credentals, which posed security risks and made deployment to different environments more difficult. CRUD operations were implemented but lacked separation of concerns, meaning the database logic was tightly coupled with the application’s presentation layer.

This version serves as the baseline for comparing later enhancements that introduced modular design, secure credential handling, and improved maintainability.

## Key Features
- Built using Jupyter Notebook with direct database connection.
- Contained hardcoded database credentials in the code.
- CRUD operations for interacting with the MongoDB collection.
- Single-file design, with UI and backend logic combined.

## Limitations in Original
- Credentials stored in plain text within the code.
- No modular code structure — all logic and UI in one file.
- No logging or error handling for failed operations.
- Limited reusability and maintainability.

