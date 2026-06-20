from managers.students_manager import StudentsManager
from models.students import UpdateStudent
SM=StudentsManager()
US=UpdateStudent()
def menu():
    print('\n ---Student Management System---')
    print("1. Add student")
    print("2. View Student")
    print("3. Update Student")

while True:
    menu()
    choice=input('Enter choice :')

    # create student
    if choice=='1':

        name = input("Enter name: ")
        age = (input("Enter age: "))
        class_no = (input("Enter class no: "))
        roll = (input("Enter roll: "))
        gender = input("Enter gender: ")
        department = input("Enter department: ")
        address = input("Enter address: ")
        email = input("Enter email: ")
        phone_number = input("Enter phone: ")
        s=name,age,class_no,roll,gender,department,address,email,phone_number
        SM.createStudent(s)

    # view student
    elif choice=='2':
        SM.view_student()

    # Update Student
    elif choice=='3':
        class_no = input("Enter student previous  class no: ")
        roll = input("Enter student previous  roll: ")
        if not class_no.isdigit() or not roll.isdigit():
            print("Class and Roll must be Number.")
            continue
        n_class_no=int(class_no)
        n_roll=int(roll)
        if n_class_no <=0 or n_roll <=0 :
            print('Invalid Class_no and Roll.')
            continue  
        result=SM.search_one_student(n_class_no,n_roll)

        value=result['student']
        msg=result['msg']   

        if not msg:
            print('Student not found!',msg)
            continue

        print(value,"successful")    
        find_id=value[10]
        name =US.get_value("name", value[1]) 
        age = US.get_value("age",value[2])  
        class_no = US.get_value("class_no",value[3])  
        roll = US.get_value("roll",value[4]) 
        gender = US.get_value("gender",value[5]) 
        address =  US.get_value("address",value[6]) 
        email = US.get_value("email",value[7]) 
        phone_number =US.get_value("phone_number",value[8]) 
        department =US.get_value("department",value[9])   
        s =name,str(age),str(class_no),str(roll),gender,address,department,email,phone_number
       
        SM.updateStudent(find_id,s)








