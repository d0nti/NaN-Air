
HEADER_AIRPLANES= (
      "------------------------------"
    + "\n"
    + "  NaN Air - Manage Airplanes"
    + "\n"
    + "------------------------------"
)


class Airplanes:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def airplanes_menu_output(self):
        print(HEADER_AIRPLANES)
        print("1. Register Airplane")
        print("2. Display Airplanes")
        print("3. Find Airplane")
        print("4. Print Airplane Efficiency")
        print("b. Back")
        print("q. Quit")

    def input_prompt_airplanes(self):
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

            else:
                print("Invalid input! Please try again.")