from managers.students_manager import StudentsManager
from models.students import UpdateStudent
SM=StudentsManager()
US=UpdateStudent()
def menu():
    print('\n ---Student Management System---')
    print("1. Add student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Upload Document")
    print("5. Search Student")
    print("6. Search students by class")
    print("7. View Student Documents")
    print("8. Delete Student")

while True:
    menu()
    choice=input('Enter choice :')

    # create student
    if choice=='1':

        name = input("Enter name: ")
        age = input("Enter age: ")
        class_no = input("Enter class no: ")
        roll = input("Enter roll: ")
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

        value=SM.get_student_by_class_roll(class_no,roll)
        if not value:
            continue
        find_id=value[10]
        student_id=value[0]
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
       
        SM.updateStudent(find_id,student_id,s)

    # Upload document
    elif choice=='4':
        # First upload your document in the uploads folder.Then
        # Enter file name: 'Like - photo.jpg '

        class_no = input("Enter student previous  class no: ")
        roll = input("Enter student previous  roll: ")
        value=SM.get_student_by_class_roll(class_no,roll)
        
        if not value:
            continue

        student_pk=value[10]
        file_name=input("Enter file name: ")
        SM.upload_documents(student_pk,file_name)

 

    # Search Student
    elif choice=='5':
        class_no = input("Enter student class no: ")
        roll = input("Enter student  roll: ")
        result=SM.search_one_student(class_no,roll)
        student=result['student']
        print(student[:-1])

    # Search Student By class
    elif choice=='6':
        class_no=int(input("Enter the class no: "))
        result=SM.search_students_by_class(class_no)
        for r in result:
            print(r)
        
    # View student documents
    elif choice=='7':
        pass

    # Delete Student
    elif choice=='8':
        class_no = input("Enter student previous  class no: ")
        roll = input("Enter student previous  roll: ")

        value=SM.get_student_by_class_roll(class_no,roll)
        SM.deleteStudent(value[10])


        




