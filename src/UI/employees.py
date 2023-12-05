HEADER_EMPLOYEES = (
      "------------------------------"
    + "\n"
    + "  NaN Air - Manage Employees"
    + "\n"
    + "------------------------------"
)

HEADER_INPUT_1 =(
      "------------------------------"
    + "\n"
    + "  NaN Air - Employee List"
    + "\n"
    + "------------------------------"
)

HEADER_INPUT_2 =(
      "------------------------------"
    + "\n"
    + "  NaN Air - Pilot List"
    + "\n"
    + "------------------------------"
)

HEADER_INPUT_3 =(
      "------------------------------"
    + "\n"
    + "  NaN Air - Flight Attendant List"
    + "\n"
    + "------------------------------"
)

HEADER_INPUT_4 =(
      "------------------------------"
    + "\n"
    + "  NaN Air - Heads of Service List"
    + "\n"
    + "------------------------------"
)

HEADER_INPUT_5 =(
      "------------------------------"
    + "\n"
    + "  NaN Air - Register New Employee"
    + "\n"
    + "------------------------------"
    + "Please Enter the Following Information:"
    + "\n"
    + "Employee Name, Employee SSID, Job Title, Pilot License (If applicable), Home Address, Phone Number, E-mail Address, Home Phone Number (optional)"
)

class Employees:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def employees_menu_output(self):
        print(HEADER_EMPLOYEES)
        print("1. Employees")
        print("2. Register New Employee")
        print("3. Shift Plan")
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
                self.list_employees()

            elif command == "2" or command == "2.":
                pass

            elif command == "3" or command == "3.":
                pass
            
            else:
                print("Invalid input! Please try again.")


    def list_employees(self):
        print(HEADER_INPUT_1)
        print("1. List or edit Pilots")
        print("2. List or edit Flight Attendence")
        print("3. View Shift Plan")
        print("b. Back")
        print("q. Quit")
        self.logic_wrapper.get_all_employees() # ÞETTA VIRKAR !! YAAAAY!!
        
        
