from Add_task import add_description
from View_Task import view
from Mark_As_Completed import mark_as_completed

print("\t\tWELCOME TO PYTHON E-NOTES APPLICATION")

def main_fun():
    check = True
    while check:
        menu = input("MENU:\n1) Add Task (Press 1)\n2) View Tasks (Press 2)\n3) Mark as Completed Task (Press 3)\n4) Quit (Press 4)\n Enter Yours Choice:")
        if menu == '1' or menu.lower()=="add task":
            add_description()
            check = False
            main_fun()

        elif menu == '2' or menu.lower()=="view task":
            view()
            check = False
            main_fun()


        elif menu == '3' or menu.lower()=="mark as completed task":

            mark_as_completed()
            check = False
            main_fun()


        elif menu == '4'or menu.lower()=="quit":
            print("Thanks For Using our Application !!!")
            check = False
        

        else:
            print("Please choose from the above mentioned list")
            main_fun()


main_fun()