# CS-499-Capstone – Animal Shelter MongoDB Dashboard

<p align="center">
  <img src="data/Grazioso%20Salvare%20Logo.png" alt="Grazioso Salvare Logo" width="200">
</p>

This repository contains my enhanced CS 499 Capstone project.  
It is based on the Animal Shelter Dashboard originally developed in CS 340 and enhanced to improve **Software Design**, **Algorithms & Data Structures**, and **Database Integration**. While all my enhancements used the same original files, each category focuses on a different aspect of improvement.

---

## 📂 Project Structure
- [original_code/](original_code) – Original CS 340 project files  
- [enhanced_code/](enhanced_code) – Enhanced CS 499 Capstone project files  
- [software-enhancement/](software-enhancement) – Narrative and details for Software Design & Engineering category  
- [algorithms-enhancement/](algorithms-enhancement) – Narrative and details for Algorithms & Data Structures category  
- [databases-enhancement/](databases-enhancement) – Narrative and details for Databases category  
- [code-review/](code-review) – Code review video and narrative  

---
## 🛠️ Prerequisites
- Python 3.10+
- MongoDB (local or cloud instance)
- Recommended: MongoDB Compass

Here’s your **Installation** section rewritten cleanly so everything is clickable, step-by-step, and ready to paste into your README:

````markdown
## 📦 Installation

1. **Clone the repository**  
   [GitHub Repository](https://github.com/GregoriaRamirez/CS-499-Capstone)  
   ```bash
   git clone https://github.com/GregoriaRamirez/CS-499-Capstone.git
   cd CS-499-Capstone/enhanced_code
````
2. python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. **Create a `.env` file** in the `enhanced_code` folder with:

   ```env
   MONGO_USER=your_username
   MONGO_PASS=your_password
   MONGO_HOST=localhost
   MONGO_PORT=27017
   MONGO_DB=aac
   MONGO_COL=animals
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**

   ```bash
   python app.py
   ```

6. **Open the dashboard** in your browser:
   [http://127.0.0.1:8050](http://127.0.0.1:8050)

---

## 🎥 Code Review Video

[▶️ Watch the Code Review on YouTube](https://www.youtube.com/watch?v=DXgBW47WSRQ)
