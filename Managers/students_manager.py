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
        return student

    def updateStudent(self,student):
        stu=StudentDB()
        _id=student.find_id
        name =student.name
        age = student.age
        class_no =student. class_no
        roll = student.roll
        gender =student.gender
        department =student.department
        address =student.address
        email =student.email
        phone_number=student.phone_number

        up_student=name,age,class_no,roll,gender,department,address,email,phone_number

        valid,msg=Validator.updateValidatorInput(up_student)
        if(valid):
            print('ok ',up_student, _id)
            # stu.updateStudent(_id,up_student)
            # stu.close_connection()
        else:
            print(msg)
            stu.close_connection()    
        
             
