from db_connection import get_connect
from datetime import datetime
from Models.students import Student

class StudentDB:

    # database connection
    def __init__(self):

        try:
            self.conn=get_connect()
            self.cur=self.conn.cursor()
            print('Connected!')
        except Exception as e:
            print('Database connection fail!')
            print(e)
    
    def genarate_student_id(self,class_no,roll):
        return

    def create_student(self,student):
        self.genarate_student_id()
        query="""INSERT INTO students(
                  
                  
                  )"""
        print('create student')
        return
    

    def close_connection(self):
        self.cur.close()
        self.conn.close()
        print("Connection Closed")

name = input("Enter name: ")
age = int(input("Enter age: "))
class_no = int(input("Enter class no: "))
roll = int(input("Enter roll: "))
gender = input("Enter gender: ")
depart = input("Enter department: ")
address = input("Enter address: ")
email = input("Enter email: ")
phone_number = input("Enter phone: ")
s1=Student(name,age,class_no,roll,gender,depart,address,email,phone_number)
stu=StudentDB()
stu.genarate_student_id(class_no,roll)
stu.create_student(s1)
stu.close_connection()
