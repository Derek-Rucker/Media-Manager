import sqlite3


def create_connection(db_file):
    conn = None
    try: 
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """
    create a table
    :param conn: connection object
    :param create_table_sql: a create table statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

