import sqlite3
connection = sqlite3.connect("Notes_Created.db")
cursor = connection.cursor()

# cursor.execute("DROP TABLE IF EXISTS Notes")
# cursor.execute(
#     "CREATE TABLE notes (count INTEGER PRIMARY KEY, description TEXT NOT NULL, status TEXT NOT NULL)")


def add_description():

    description = input("Please Enter your task description :\n")
    default_status = "Not Completed Yet"

    cursor.execute("SELECT * FROM notes")
    count = len(cursor.fetchall())
    count += 1

    cursor.execute("INSERT INTO notes VALUES (?,?,?)",
                   (count, description, default_status))
    print("Description of your task is Added !")

    connection.commit()
    connection.close()
