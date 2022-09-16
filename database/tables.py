from sqlite3 import Error
from connection import create_connection

database = r"C:\Development\Media-Manager\media-database.db"

def create_tables():
    
    sql_create_movies_table = """CREATE TABLE IF NOT EXISTS movies (
                                id integer PRIMARY KEY,
                                title text NOT NULL,
                                director text,
                                year text,
                                description text
                            );"""
                            
    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_movies_table)
    else:
        print("Cannot create the db connection.")

def create_table(conn, create_table_sql):
    """
    create a table
    :param conn: connection object
    :param create_table_sql: a create table statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
