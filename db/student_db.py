from db.db_connection import get_connect
from datetime import datetime
from models.students import Student

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
        year=datetime.now().year
        student_id=f"{year}{class_no}{roll}"
        return student_id

    def create_student(self,student):
        try:
            student_id=self.genarate_student_id(student.class_no,student.roll)
            print(student_id)
            query="""INSERT INTO students(
                student_id,
                name,
                age,
                class_no,
                roll,
                gender,
                department,
                address,
                email,
                phone_number 
                )                  
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                  """
            values=(
                student_id,
                student.name,
                student.age,
                student.class_no,
                student.roll,
                student.gender,
                student.department,
                student.address,
                student.email,
                student.phone_number 
        )          
            
            self.cur.execute(query,values)
            self.conn.commit()
            print('Student created successfully!')
        except Exception as e:
            print("Student creation failed!")
            print(e)

        
        

    def close_connection(self):
        self.cur.close()
        self.conn.close()
        print("Connection Closed")

