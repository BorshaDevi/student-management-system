<h1>Student Management System<h1>
<p>A simple and efficient **Student Management System** built with **Python**. This project helps manage student records, interact with a SQL database, and upload/store student documents in an organized way.</p>

## Features

- **Student Data Management**
  - Add new student records.
  - Update existing student information.
  - View student details.
  - Search students by ID or class.
  - Delete student records.

- **Database Integration**
  - Store student information permanently using an SQL database.

- **Modular Architecture**
  - Organized using **Managers** and **Models** for better code structure and maintainability.

- **Document Management**
  - Upload and store student documents.
  - Manage uploaded files inside dedicated folders.

---




##  Project Structure

```text
student-management-system/
│
├── Managers/
│   └── students_manager.py
│
├── Models/
│   ├── inputValid.py
│   └── students.py
│
├── db/
│   ├── db_connection.py
│   └── student_db.py
│
├── documents/
│   ├── Screenshot.png
│   └── s1 certificate.png
│
├── sql/
│   └── schema.sql
│
├── uploads/
│   ├── Screenshot.png
│   └── s1 certificate.png
│
├── .gitignore
├── README.md
└── main.py
```