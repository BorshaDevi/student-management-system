from db_connection import get_connect
from datetime import datetime

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
    
    def genarate_student_id(self):
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


stu=StudentDB()
stu.create_student()
stu.close_connection()
