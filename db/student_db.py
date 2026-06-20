from db.db_connection import get_connect
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

# genarate  student  id

    def genarate_student_id(self,class_no,roll):
        year=datetime.now().year
        student_id=f"{year}{class_no}{roll}"
        return student_id
        
# create student

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
                int(student.age),
                int(student.class_no),
                int(student.roll),
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

        
# view students

    def view_students(self):
        query="""SELECT * FROM students"""
        self.cur.execute(query)
        students=self.cur.fetchall()
        for s in students:
            print(s)
# Search student

    def search_one_student(self,class_no,roll):
        try:
            query="""SELECT  * FROM students
            WHERE class_no= %s
            AND roll= %s
            """
            value=(
            class_no,
            roll
            )
            self.cur.execute(query,value)
            student=self.cur.fetchone()
            if student:
                return {'student':student,
                        'msg':True}
            else:
                return {
                        'student':None,
                        'msg':False
                       }            
        except Exception as e:
            print("Student search failed!")
            print(e)


        

# Update
 
    def updateStudent(self,find_id,student_id,student):
        result=self.search_one_student(student.class_no,student.roll)
        if result['msg']:
            student_id=student_id
        else:
             student_id=self.genarate_student_id(student.class_no,student.roll)   
        try:
            query=""" UPDATE students
            set student_id=%s,
                name=%s,
                age=%s,
                class_no=%s,
                roll=%s,
                gender=%s,
                department=%s,
                address=%s,
                email=%s,
                phone_number=%s
            WHERE id=%s     
            """
            value=(
                student_id,
                student.name,
                int(student.age),
                int(student.class_no),
                int(student.roll),
                student.gender,
                student.department,
                student.address,
                student.email,
                student.phone_number,
                find_id
            )
            self.cur.execute(query,value)
            self.conn.commit()
            print('Student Updated Successfully!')
        except Exception as e:
            print("Student update failed!")
            print(e)

       
    def close_connection(self):
        self.cur.close()
        self.conn.close()
        print("Connection Closed")

