from dotenv import load_dotenv
import mysql.connector
import os

def create_connetion():
    load_dotenv()
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return conn

def db_query(query:str):
    with create_connetion() as conn:
        curs = conn.cursor()
        curs.execute(query)
        result = curs.fetchall()
        return result
    
def db_query_single(query: str):
    with create_connetion() as conn:
        curs = conn.cursor()
        curs.execute(query)
        result = curs.fetchone()
        return result

def db_insert(table_name:str, col_names:list, values: list):
    with create_connetion() as conn:
        curs = conn.cursor()
        val_str = ",".join(["%s" for _ in col_names])
        command = f"insert into {table_name} ({", ".join(col_names)}) values ({val_str})"
        curs.executemany(command, values)
        conn.commit()

