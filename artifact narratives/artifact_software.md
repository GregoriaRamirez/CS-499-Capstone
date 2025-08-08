# 🛠️ Software Design & Engineering Artifact

## 📌 Artifact Description

For my CS 499 Capstone, I chose to enhance my final project from CS 340: Client-Server Development. Originally created in February 2025, the artifact is a web-based dashboard for an animal shelter. The application was first developed in a Jupyter Notebook using Python, Dash, and a MongoDB database connected to a CSV data source. It displayed outcome records from the shelter in a table, supported search and filtering, and included simple charts for visual analysis.

I selected this artifact because it integrates several skills I have developed throughout the program: database operations, data manipulation with pandas, and interactive web development with Dash. The original version functioned, but it lacked structure, performance optimizations, and security. This made it an ideal candidate for enhancement.

To improve the software design, I reorganized the code into a more modular format using a Model-View-Controller (MVC) approach. I separated the routing logic, callback functions, and layout components into their own files. This structure improved readability, scalability, and ease of testing. I also implemented environment variables using python-dotenv to store sensitive information like the MongoDB connection string, enhancing security and aligning with industry best practices.

In addition to reorganizing the architecture, I introduced new filtering features, including color and breed filters, which expanded the application's usability. These enhancements improved the dashboard’s responsiveness by limiting the data processed client-side and reducing visual clutter. The filtering logic was refactored to be more efficient, using conditional logic and vectorized operations in pandas, which improved both performance and maintainability.

## 📎 Justification for Inclusion

To improve the software design, I reorganized the code into a more modular format using a Model-View-Controller (MVC) structure. I separated the routing logic, callback functions, and layout components into separate files. This made the codebase easier to read, scale, and test. I also used `python-dotenv` to manage environment variables and securely store sensitive information like the MongoDB connection string—an improvement aligned with industry standards.

Beyond restructuring the architecture, I added new filtering features for animal color and breed. These expanded the dashboard’s usability and helped reduce clutter by narrowing down results. I also refactored the filtering logic using conditional checks and vectorized operations in pandas, which made the app faster and more efficient.

At the start of the enhancement, I focused on two outcomes:

- **Outcome 3 – Software Design and Engineering:** Met by refactoring the codebase into modular components, applying the MVC pattern, and improving security practices.
- **Outcome 4 – Algorithms and Data Structures:** Met by improving filtering logic and implementing efficient data-handling techniques.

As the project progressed, I realized I had also met:

- **Outcome 5 – Databases:** I transitioned from using the Mongo shell to MongoDB Compass, which gave me a more secure and user-friendly way to manage the database. I also added error handling, replaced static CSV imports with live MongoDB queries, and ensured proper connection management in the code.

One challenge I faced was reorganizing the file structure without breaking the app. I had to carefully adjust import paths and retest each callback to confirm it worked. Another challenge was setting up a virtual environment with `venv` to isolate dependencies and avoid version conflicts. That step helped streamline future testing and deployment.

Overall, this project reflects how far I have come in applying real-world development standards, organizing code for long-term maintainability, and building a working product that is secure, efficient, and user-friendly.

## 🧠 Reflection on Software Engineering Skills

This enhancement demonstrates my ability to:

- Apply modular design for scalability and reusability
- Follow secure coding practices
- Refactor academic code into maintainable, professional-grade applications
- Use tools like VS Code and `.env` to build software suitable for real-world deployment
- Implement the MVC pattern by separating layout, callbacks, and data logic into distinct modules
- Introduce efficient filter logic using vectorized operations in pandas
- Add user-friendly features like breed and color filtering
- Create a virtual environment using `venv` to manage dependencies cleanly
- Transition from static data files to secure, real-time database queries using MongoDB Compass
- Handle database errors gracefully and ensure connections are opened and closed properly

## 📁 Project Folder Structure (After Enhancement)

CS499Capstone/
├── app.py # Launches the Dash application
├── controller.py # Handles Dash callbacks and routing logic
├── .env # MongoDB credentials (secured)
├── requirements.txt # Dependency list for virtual environment
├── README.md # Project documentation
├── .gitignore # Excludes venv and .env from Git
│
├── model/
│ ├── init.py # Initializes the model module
│ ├── model.py # MongoDB access and CRUD logic
│ └── view.py # Layout and view logic for Dash app
│
├── assets/
│ ├── Dashboard.png
│ ├── DashChartGeo.png
│ ├── Grazioso Salvare Logo.png
│ └── SelectBreed.png
│
├── original_code/ # Backup of the original unenhanced project
└── venv/ # Virtual environment for isolating dependencies


## 🎓 Course Outcomes Met

- **Outcome 3 (Software Design and Engineering):** Achieved by implementing modularity, using environment variables, and improving code structure and maintainability.
- **Outcome 4 (Algorithms and Data Structures):** Achieved by optimizing filtering logic and using efficient pandas operations.
- **Outcome 5 (Databases):** Achieved through secure MongoDB integration, query handling, and transition from static CSV to live database access.

## 🔗 Project Links

- [Original Code Folder](./original_code)
- [Enhanced Code Folder](./enhanced_code)
- [Video Walkthrough](https://www.youtube.com/embed/NTrtEVuawBM)
- ![Screenshot](./assets/Animal_Shelter_Dashboard.png)


