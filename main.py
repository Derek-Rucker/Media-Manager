from sqlite3 import Error
from database.connection import create_connection

def main():
    database = r"C:\Development\Media-Manager\database\media-database.db"

    conn = create_connection(database)

    if conn is not None:
        cursor = conn.cursor()
        while True:
            print("Welcome to media manager!")
            print("1. View Movies")
            print("2. Add Movie to Database")
            print("3. Exit")
            selection = int(input("Please make a selection: "))
            
            if selection == 1:
                select_command = "SELECT * FROM movies"
                cursor.execute(select_command)
                print(cursor.fetchone())
            elif selection == 2:
                movie_title = input("Title: ")
                director = input("Director: ")
                year_released = input("Release Year: ")
                description = input("Description: ")
                insert_command = f"""INSERT INTO movies(title, director, year, description) 
                                    VALUES('{movie_title}', '{director}', '{year_released}', '{description}');"""
                try:
                    if cursor.execute(insert_command):
                        print("Movie added succesfully!")
                    conn.commit()
                except Error as e:
                    print(e)
            elif selection == 3:
                exit()
            else:
                print("Invalid selection")
    else:
        print("Cannot create the db connection.")


if __name__ == '__main__':
    main()
    