from managers.students_manager import StudentsManager
SM=StudentsManager()
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
        class_no=int(class_no)
        roll=int(roll)
        if class_no <=0 or roll <=0 :
            print('Invalid Class_no and Roll.')
            continue   
        msg=SM.search_student(class_no,roll)
        # name = input("Enter name: ") 
        # age = (input("Enter age: "))
        # class_no = (input("Enter class no: "))
        # roll = (input("Enter roll: "))
        # gender = input("Enter gender: ")
        # department = input("Enter department: ")
        # address = input("Enter address: ")
        # email = input("Enter email: ")
        # phone_number = input("Enter phone: ")
        # s=name,age,class_no,roll,gender,department,address,email,phone_number
        # SM.updateStudent(s)








