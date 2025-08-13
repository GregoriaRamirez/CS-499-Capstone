# CS-499-Capstone – Animal Shelter MongoDB Dashboard

<p align="center">
  <img src="data/Grazioso%20Salvare%20Logo.png" alt="Grazioso Salvare Logo" width="200">
</p>

This repository contains my enhanced CS 499 Capstone project.
It is based on the Animal Shelter Dashboard originally developed in CS 340 and enhanced to improve Software Design, Algorithms & Data Structures, and Database Integration. All enhancements were applied to the same set of original project files, adapted to meet the specific goals of each category.

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

---

## 📦 Installation
1. **Clone the repository**  
   ```bash
   git clone https://github.com/GregoriaRamirez/CS-499-Capstone.git
   cd CS-499-Capstone/enhanced_code
````

2. **Create a `.env` file** in the project root with:

   ```env
   MONGO_USER=your_username
   MONGO_PASS=your_password
   MONGO_HOST=localhost
   MONGO_PORT=27017
   MONGO_DB=aac
   MONGO_COL=animals
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the Project

From the `enhanced_code` folder, run:

```bash
python app.py
```

Then open your browser to:

```
http://127.0.0.1:8050
```

---

## 🎥 Code Review Video

[▶ Watch on YouTube](https://www.youtube.com/watch?v=DXgBW47WSRQ)

---

## 📄 Documentation

* [Software Design & Engineering Enhancement](software-enhancement/README.md)
* [Algorithms & Data Structures Enhancement](algorithms-enhancement/README.md)
* [Databases Enhancement](databases-enhancement/README.md)
* [Code Review](code-review/README.md)



