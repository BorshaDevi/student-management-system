from models.students import Student
from db.student_db import StudentDB
from models.inputValid import Validator
class StudentsManager:
    def createStudent(self,student):
        s1=Student(*student)
        stu=StudentDB()
        valid,msg=Validator.validatorInput(s1)
        if(valid):
            stu.create_student(s1)
            stu.close_connection()
        else:
           print(msg)
           stu.close_connection()
             
