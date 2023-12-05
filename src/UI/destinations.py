from Logic.UILogicWrapper import UI_Logic_Wrapper

INVALID_INPUT = "Invalid input! Please try again."
QUIT_MESSAGE = "Bye Bye!"

HEADER_DESTINATIONS = (
      "------------------------------"
    + "\n"
    + "  NaN Air - {}"
    + "\n"
    + "------------------------------"
)


class Destinations:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper
        
        
    def destinations_menu_output(self):
        print(HEADER_DESTINATIONS.format("Manage Destinations"))
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
                print(QUIT_MESSAGE)
                break

            elif command == "b" or command == "b.":
                break

            elif command == "1" or command == "1.":
                self.list_destinations()

            elif command == "2" or command == "2.":
                pass

            elif command == "3" or command == "3.":
                pass

            else:
                print(INVALID_INPUT)


    def list_destinations(self):
        print(HEADER_DESTINATIONS.format("Destinations"))
        destinations = self.logic_wrapper.get_all_destinations()

    def register_destination(self):
        print(HEADER_DESTINATIONS.format("Register Destination"))
        
