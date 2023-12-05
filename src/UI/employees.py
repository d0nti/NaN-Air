HEADER_EMPLOYEES = (
      "------------------------------"
    + "\n"
    + "  NaN Air - Manage Employees"
    + "\n"
    + "------------------------------"
)

HEADER_INPUT_2 =(
    "------------------------------"
    + "\n"
    + "  NaN Air - Employee List"
    + "\n"
    + "------------------------------"
)



class Employees:
    def __init__(self):
        self.employees_menu_output()
        
    def employees_menu_output(self):
        print(HEADER_EMPLOYEES)
        print("1. List All or Edit Employees")
        print("2. List All or Edit Pilots")
        print("3. List All or Edit Flight Attendants")
        print("4. List All or Edit Heads of Service")
        print("5. Register New Employee")
        print("6. Shift Plan")
        print("7. Search")
        print("b. Back")
        print("q. Quit")

    def input_prompt_employees(self):
        while True:
            command = input("User Input: ")
            command = command.lower()
            if command == "q" or command == "q.":
                print("Bye Bye!")
                break
            elif command == "b" or command == "b.":
                break
            elif command == "1" or command == "1.":
                pass
            elif command == "2" or command == "2.":
                pass
            elif command == "3" or command == "3.":
                pass
            elif command == "4" or command == "4.":
                pass
            elif command == "5" or command == "5.":
                self.register_employee(self)
            elif command == "6" or command == "6.":
                pass
            elif command == "7" or command == "7.":
                pass
            else:
                print("Invalid input! Please try again.")


<<<<<<< Updated upstream
    def input_2(self):
        print(HEADER_INPUT_2)
        while True:
            command = input("User Input: ")
            command = command.lower()
            if command == "q" or command == "q.":
                print("Bye Bye!")
                break
            elif command == "b" or command == "b.":
                break
            elif command == "1" or command == "1.":
                pass
            elif command == "2" or command == "2.":
                pass
=======
    def register_employee(self):
        pass
>>>>>>> Stashed changes
