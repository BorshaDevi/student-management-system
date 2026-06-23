CREATE TABLE students(
    student_id BIGINT UNIQUE,
    name VARCHAR (350),
    age SMALLINT ,
    class_no INT,
    roll INT,
    gender VARCHAR(20),
    department VARCHAR(150),
    email VARCHAR(250),
    phone_number VARCHAR(14),
    address VARCHAR(400),
    id SERIAL  PRIMARY KEY
)

CREATE TABLE student_file(
    _id SERIAL PRIMARY KEY,
    student_pk INT,
    file_name TEXT,
    file_path TEXT,
    FOREIGN KEY (student_pk) REFERENCES students(id)
)