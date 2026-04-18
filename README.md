Student Management API (FastAPI + SQLite)

Hi!
This is my first proper backend project built with FastAPI. I created this project to understand how real-world APIs are structured and how different parts of a backend system work together.
The main goal of this project is to manage student data using a clean and organized architecture.

Tech Stack 
•	Python 
•	FastAPI 
•	SQLite 
•	SQLAlchemy 

Project Structure 
app/
├── main.py
├── database.py
├── models/
│   └── student.py
├── schemas/
│   └── student.py
├── services/
│   └── student_service.py
├── routers/
│   └── student.py
I tried to follow a clean structure like real backend projects:
•	main.py → Entry point of the application
•	database.py → Database connection setup
•	models → Database tables (SQLAlchemy models)
•	schemas → Data validation using Pydantic
•	services → Business logic (kept separate from routes)
•	routers → API endpoints (handles requests & responses)
This separation helped me understand how to keep code clean and scalable.

Features
This API supports basic CRUD operations:
•	Create a new student
•	Get all students
•	Get a student by ID
•	Update student information
•	Delete a student
How to Run the Project
1.	Clone the repository 
git clone https://github.com/Khurram713/FASTAPI_PROJECTS.git

cd FASTAPI_PROJECTS
2.	Create virtual environment 
python -m venv venv
3.	Activate virtual environment 
•	Windows: 
venv\Scripts\activate
•	Mac/Linux: 
source venv/bin/activate
4.	Install dependencies 
pip install -r requirements.txt
5.	Run the server 
uvicorn app.main:app –reload

After running the server, open:
•	Swagger UI: http://127.0.0.1:8000/docs 


My Learning
•	How to structure a FastAPI project 
•	How to connect SQLite database 
•	How to separate models, schemas, services, and routes 
•	Basic CRUD operations 
Final Note
•	This project is part of my learning journey into backend development.
•	I know it’s not perfect, but I focused on understanding concepts and building something complete from scratch.
•	If you have feedback or suggestions, I’d really appreciate it!

Future Improvements
•	JWT Authentication (Login / Signup)
•	Use PostgreSQL instead of SQLite


