class Validator:
    def validatorInput(self,student):
        # Name validation
        if student.name.strip()=='':
            return (False,f'Name is required.')
        if student.name.isdigit():
            return (False,f'Name must be text.')
        
        # age validation
        if student.age.strip()=='':
            return (False,f'Age is required.')
        if not student.age.isdigit():
            return (False,f'Age is must be number')
        
        # class no validation
        if  student.class_no.strip()=='':
            return (False,f'Class no  is required.')
        if not student.class_no.isdigit():
            return (False,f'Class no  is must be number.')
        
        # Roll validation
        if student.roll.strip()=='':
            return (False,f'Roll is required.')
        if not student.roll.isdigit():
            return (False,f'Roll is must be number.')
        
        # Department validation
        if student.department.strip()=='':
            return (False,f'Department is required.')
        if student.department.isdigit():
            return (False,f'Department must be text.')
        
        # Address validation
        if student.address.strip()=='':
            return (False,f'Address  is required.')
        
        # Email validation
        if student.email.strip()=='':
            return (False,f'Email is required.')
        if '@' not in student.email:
            return (False,f'Invalid email.')
        
        # Phone Number validation
        if student.phone_number.strip()=='':
            return (False,f'Phone Number  is required.')
        if not student.phone_number.isdigit():
            return (False,f'Phone Number  must be number.')
        

        return True ,'Valid'