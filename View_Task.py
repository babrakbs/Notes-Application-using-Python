import sqlite3

connection = sqlite3.connect("Notes_Created.db")
cursor = connection.cursor()

def view():
    cursor.execute("SELECT * FROM notes")

    view_col = cursor.fetchall()
    print(view_col)
# names = list(map(lambda x: x[0], cursor.description))
# print(f"{names} \n {view_col}")
    print("<------------------------------------>")
    print("Count\tDescription\tCurrentStatus")
    print("<------------------------------------>")
    for tup in view_col:
        for item in tup:
            # print(item)
            count = tup[0]
            descp = tup[1]
            status = tup[2]
        print(f"{count}\t{descp}\t{status}")
        print("<------------------------------------>")