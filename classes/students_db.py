from db_connection import get_connect
conn=get_connect()
cur=conn.cursor()





cur.close()
conn.close()
