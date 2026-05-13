import psycopg2
from dotenv import load_dotenv
import os
load_dotenv('.env.local')
conn=psycopg2.connect(
    host=os.getenv(),
    database=os.getenv(),
    user=os.getenv(),
    password=os.getenv()
)