from UI.Utils.Constants import UIConstants


class Airplanes:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def airplanes_menu_output(self):
        print(UIConstants.HEADER.format(UIConstants.MANAGE_AIRPLANES))
        print(UIConstants.FOUR_MENU_OPTION.format(UIConstants.DISPLAY_AIRPLANES, UIConstants.REGISTER_NEW_AIRPLANE, UIConstants.FIND_AIRPLANE, UIConstants.PRINT_AIRPLANE_EFFICIENCY, UIConstants.BACK, UIConstants.QUIT))
        
        # print("1. Display Airplane")
        # print("2. Register New Airplane")
        # print("3. Find Airplane")
        # print("4. Print Airplane Efficiency")
        # print("b. Back")
        # print("q. Quit")

    def input_prompt_airplanes(self):
        while True:
            command = input("User Input: ")
            command = command.lower()

            if command == "q" or command == "q.":
                print(UIConstants.QUIT_MESSAGE)
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
                print(UIConstants.INVALID_INPUT)
                

    def list_airplanes(self):
        print(UIConstants.HEADER.format(UIConstants.DISPLAY_AIRPLANES))
        airplanes = self.logic_wrapper.get_all_airplanes()
        pass
    
    def register_new_airplane(self):
        print(UIConstants.HEADER.format(UIConstants.REGISTER_NEW_AIRPLANE))

        pass

    def find_airplane(self):
        print(UIConstants.HEADER.format(UIConstants.FIND_AIRPLANE))
        pass

    def print_airplane_efficiency(self):
        print(UIConstants.HEADER.format(UIConstants.PRINT_AIRPLANE_EFFICIENCY))
        pass