from Logic.UILogicWrapper import UI_Logic_Wrapper

HEADER_DESTINATIONS = (
      "------------------------------"
    + "\n"
    + "  NaN Air - Manage Destinations"
    + "\n"
    + "------------------------------"
)

HEADER_INPUT_1 = (
      "------------------------------"
    + "\n"
    + "  NaN Air - Destinations"
    + "\n"
    + "------------------------------"
)


HEADER_INPUT_2 = (
      "------------------------------"
    + "\n"
    + "  NaN Air - Register Destination"
    + "\n"
    + "------------------------------"
)


class Destinations:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper
        
        
    def destinations_menu_output(self):
        print(HEADER_DESTINATIONS)
        print("1. List Destinations")
        print("2. Register Destination")
        print("3. Search")
        print("b. Back")
        print("q. Quit")

    def input_prompt_destinations(self):
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

            else:
                print("Invalid input! Please try again.")


    def list_destinations(self):
        print(HEADER_INPUT_1)
        