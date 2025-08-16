# Enhanced Code – CS 499 Capstone

This folder contains the enhanced version of my Animal Shelter Dashboard project, completed for the CS 499 Capstone.  
It builds on the original CS 340 implementation by improving structure, security, and efficiency.  
The enhancements span across **Software Design & Engineering**, **Algorithms & Data Structures**, and **Database Integration**.

## 📌 Key Enhancements
- Refactored into a **modular MVC structure** (separate `model.py`, `view.py`, and `controller.py`)  
- Removed **hardcoded credentials** and replaced with environment variables stored in `.env`  
- Added **input validation** and **error handling** for reliability  
- Improved **filtering performance** with optimized pandas operations (`.isin()`, `.between()`)  
- Implemented **logging** for debugging and monitoring  
- Ensured **database connection cleanup** for stability  

## 📄 Files in This Folder
- `.env_example` – Template for environment variables  
- `__init__.py` – Initializes the module  
- `app.py` – Main Dash application entry point  
- `controller.py` – Handles user interactions and filtering logic  
- `model.py` – Handles database queries  
- `view.py` – Defines dashboard layout and components  
- `requirements.txt` – Python dependencies
