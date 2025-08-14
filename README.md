# CS-499-Capstone – Animal Shelter MongoDB Dashboard

<p align="center">
  <img src="data/Grazioso%20Salvare%20Logo.png" alt="Grazioso Salvare Logo" width="200">
</p>

## 🌐 My CS 499 ePortfolio  
[Click here to view my full ePortfolio](https://gregoriaramirez.github.io/)  

This repository contains my Southern New Hampshire University CS 499 Capstone project, which enhances my original CS 340 Animal Shelter Dashboard. 
It is based on the Animal Shelter Dashboard originally developed in CS 340 and enhanced to improve **Software Design**, **Algorithms & Data Structures**, and **Database Integration**. While all my enhancements used the same original files, each category focuses on a different aspect of improvement.

---

## 📂 Project Navigation

- [original\_code/](https://github.com/GregoriaRamirez/CS-499-Capstone/tree/main/original_code) – Original CS 340 project files
- [enhanced\_code/](https://github.com/GregoriaRamirez/CS-499-Capstone/tree/main/enhanced) – Enhanced CS 499 Capstone project files
- [software-enhancement/](https://github.com/GregoriaRamirez/CS-499-Capstone/blob/main/narratives/Software/README.md) – Narrative and details for Software Design & Engineering category  
- [algorithms-enhancement/](https://github.com/GregoriaRamirez/CS-499-Capstone/blob/main/narratives/algorithms/README.md) – Narrative and details for Algorithms & Data Structures category  
- [databases-enhancement/](https://github.com/GregoriaRamirez/CS-499-Capstone/blob/main/narratives/Databases/README.md) – Narrative and details for Databases category  
 - [🎥 Code Review Video – Watch on YouTube](https://www.youtube.com/watch?v=DXgBW47WSRQ)


````
## 🛠️ Prerequisites
- Python 3.10+
- MongoDB (local or cloud instance)
- Recommended: [MongoDB Compass](https://www.mongodb.com/try/download/compass)
- Recommended: [Visual Studio Code](https://code.visualstudio.com/)

## 📦 Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/GregoriaRamirez/CS-499-Capstone.git
   cd CS-499-Capstone/enhanced_code
````

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

   * **Windows**

     ```bash
     venv\Scripts\activate
     ```
   * **macOS/Linux**

     ```bash
     source venv/bin/activate
     ```

3. **Create a `.env` file** in the `enhanced_code` folder:

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





