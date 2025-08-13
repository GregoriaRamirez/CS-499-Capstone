# Enhanced Code – CS 499 Capstone

This folder contains the **enhanced** version of my Animal Shelter MongoDB Dashboard project, completed for my **CS 499 Capstone**.  
The enhancements apply across **Software Design & Engineering**, **Algorithms & Data Structures**, and **Database Integration**.

## 📌 Key Enhancements
- Refactored to a **modular MVC structure** (separate `model.py`, `view.py`, and `controller.py` files).
- Removed **hardcoded credentials** and replaced with environment variables stored in `.env`.
- Added **input validation** and **error handling** to prevent invalid filter selections from causing unexpected results.
- Improved **filtering performance** with optimized pandas operations (`.isin()`, `.between()`).
- Implemented **logging** for better debugging and monitoring.
- Ensured **database connection cleanup** to improve reliability.

## 📄 Files in This Folder
- `.env_example` – Template for environment variables  
- `__init__.py` – Initializes the module  
- `app.py` – Main Dash application entry point  
- `controller.py` – Handles user interactions and filtering logic  
- `model.py` – Handles database queries  
- `view.py` – Defines dashboard layout and components  
- `requirements.txt` – Python dependencies  


