import sqlite3
connection = sqlite3.connect("Notes_Created.db")
cursor = connection.cursor()


def mark_as_completed():

    task_id = int(input(("Please enter your Task Id:")))

    cursor.execute("SELECT * from notes where count=?", (task_id,),)
    record = cursor.fetchone()

    if not record:
        print("Task Not Existed !")
    else:
        print("Task Id:", record[0])
        print("Description:", record[1])
        print("Current Status:", record[2])

        if (not record[2] == 'Completed'):
            check = True
            while check:
                updated_status = input(
                    "Want this task Mark as compeleted? Y for yes and N for No: ")

                if updated_status.lower() == "y" or updated_status.lower() == "yes":
                    cursor.execute("UPDATE notes SET status=?",
                                   ('Completed',),)
                    print("Status set to Completed!")
                    connection.commit()
                    check = False

                elif updated_status.lower() == "n" or updated_status.lower() == "no":
                    print("No changes Made !")
                    check = False

                else:
                    print("Please enter valid character !")
