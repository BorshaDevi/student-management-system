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
        msg=SM.search_one_student(n_class_no,n_roll)
       
        if not msg:
            
            print('Student not found!')
            continue

        print(msg,"successful")    
        find_id=msg[10]
        name =US.get_value("name", msg[1]) 
        age = US.get_value("age",msg[2])  
        class_no = US.get_value("class_no",msg[3])  
        roll = US.get_value("roll",msg[4]) 
        gender = US.get_value("gender",msg[5]) 
        address =  US.get_value("address",msg[6]) 
        email = US.get_value("email",msg[7]) 
        phone_number =US.get_value("phone_number",msg[8]) 
        department =US.get_value("department",msg[9])   
        s =name,str(age),str(class_no),str(roll),gender,address,department,email,phone_number
       
        SM.updateStudent(find_id,s)








