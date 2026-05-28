from models.students import Student
from db.student_db import StudentDB
from models.inputValid import Validator

# create student

name = input("Enter name: ")
age = int(input("Enter age: "))
class_no = int(input("Enter class no: "))
roll = int(input("Enter roll: "))
gender = input("Enter gender: ")
department = input("Enter department: ")
address = input("Enter address: ")
email = input("Enter email: ")
phone_number = input("Enter phone: ")
s1=Student(name,age,class_no,roll,gender,department,address,email,phone_number)
stu=StudentDB()
valid=Validator(s1)
if(valid):
    stu.create_student(s1)
else:
   print(valid)
# view student
stu.view_students()


stu.close_connection()
