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
    
    def search_one_student(self,class_no,roll):
        stu=StudentDB()
        student=stu.search_one_student(class_no,roll)
        stu.close_connection()
        return {'student':student['student'],
                'msg':student ['msg']
                }

    def get_student_by_class_roll(self,class_no,roll):
        if not class_no.isdigit() or not roll.isdigit():
            print("Class and Roll must be Number.")
            return None
        n_class_no=int(class_no)
        n_roll=int(roll)
        if n_class_no <=0 or n_roll <=0 :
            print('Invalid Class_no and Roll.')
            return None  
        result=self.search_one_student(n_class_no,n_roll)

        value=result['student']
        msg=result['msg']   

        if not msg:
            print('Student not found!')
            return None
        
        return value
            
    
    def updateStudent(self,find_id,student_id,student):
        stu=StudentDB()
        s1=Student(*student)
        valid,msg=Validator.updateValidatorInput(s1)
        if(valid):  
            stu.updateStudent(find_id,student_id,s1)
            stu.close_connection()
        else:
            print(msg)
            stu.close_connection()    
        
             
