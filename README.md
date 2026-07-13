<h1>Student Management System</h1>

<p>A modular Student Management System built with Python and SQL, featuring a clean architecture for managing student records, database queries, and document storage efficiently.
</p>

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

## Tech Stack

- **Programming Language:** Python
- **Database:** SQL (PostgreSQL)
- **Database Connector:** psycopg2

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/BorshaDevi/student-management-system.git
```

### 2. Navigate to the project directory

```bash
cd student-management-system
```

### 3. Install the required dependencies

```bash
pip install psycopg2
```

### 4. Configure the database

- Create the required database.
- Run the SQL script from the `sql/` folder to create the necessary tables.
- Update the database connection settings if needed.

### 5. Run the application

```bash
python main.py
```

## Requirements

- Python 3.10+
- PostgreSQL
- psycopg2




## Run the Application

Start the application by running the following command:

```bash
python main.py
```

### Example Usage

```text
--- Student Management System ---

1. Add Student
2. View Student
3. Update Student
4. Upload Document
5. Search Student
6. Search Students by Class
7. View Student Documents
8. Delete Student

Enter your choice: 1

Enter class (9/10/11/12): 10
Enter name: John Doe
Enter age: 18
Enter roll: 101
Enter gender: Male
Enter department: Science
Enter address: City Name
Enter email: johndoe@example.com
Enter phone: +1234567890

Student added successfully.
```
<h1>Concepts Used</h1>

<ul>
<p>Python</p>

<li>Object-Oriented Programming (OOP)</li>
<li>Modular Programming</li>
<li>Import System</li>
<li>Control Flow (Loops)</li>
<li>File Handling</li>
<li>Database Integration</li>
<li>Data Modeling</li>

<p>SQL</p>
<li>SQL Schema Creation</li>
<li>Database Queries</li>
<li>Database Connectivity</li>
</ul>


<hr></hr>

<p>
Building Dreams With Code.
</p>
---------------------------------
<p>
Happy coding journey...😊
</p>