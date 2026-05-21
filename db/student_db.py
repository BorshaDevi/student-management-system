from db_connection import get_connect

class StudentDB:

    # database connection
    def __init__(self):

        try:
            self.conn=get_connect()
            self.cur=self.conn.cursor()
            print('Connected!')
        except Exception as e:
            print('Database connection fail!')
            print(e)

    def create_student(self,student):
        query="""INSERT INTO create_student(
                  
                  
                  )"""
        print('create student')
        return
    

    def close_connection(self):
        self.cur.close()
        self.conn.close()
        print("Connection Closed")


stu=StudentDB()
stu.create_student()
stu.close_connection()
