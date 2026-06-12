from models.students import Student
from db.student_db import StudentDB
from models.inputValid import Validator


class StudentsManager:
    
    def createStudent(self,student):
        stu=StudentDB()
        s1=Student(*student)
        valid,msg=Validator.validatorInput(s1)
        if(valid):
            stu.create_student(s1)
            stu.close_connection()
        else:
           print(msg)
           stu.close_connection()


    def view_student(self):
        stu=StudentDB()
        stu.view_students()
        stu.close_connection()


    def updateStudent(self,student):
        stu=StudentDB()
        valid,msg=Validator.updateValidatorInput(stu)
        if(valid):
            stu.updateStudent(update)
            stu.close_connection()
        else:
            print(msg)
            stu.close_connection()    
        
             
