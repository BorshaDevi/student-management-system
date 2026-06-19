class Student:
    def __init__(self,name,age,class_no,roll,gender,address,department,
                      email='Null',phone_number='Null'):
            self.name=name
            self.age=age
            self.gender=gender
            self.department=department     
            self.email=email
            self.phone_number=phone_number
            self.address=address
            self.class_no=class_no
            self.roll=roll

class UpdateStudent:
    def __init__(self,name=None,age=None,class_no=None,roll=None,gender=None,
                           address=None,department=None,email=None,phone_number=None):
            self.name=name
            self.age=age
            self.gender=gender
            self.department=department     
            self.email=email
            self.phone_number=phone_number
            self.address=address
            self.class_no=class_no
            self.roll=roll
