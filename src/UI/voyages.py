from UI.Utils.Constants import UIConstants


class Voyages:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def voyages_menu_output(self):
        # PRENTAR MENU-IÐ .  <---- PUNKTUR
        print(UIConstants.HEADER.format(UIConstants.MANAGE_VOYAGES))
        print(UIConstants.SORT_BY_MENU.format(UIConstants.DISPLAY_VOYAGES, UIConstants.REGISTER_NEW_VOYAGE, UIConstants.POPULATE_VOYAGE, UIConstants.CHECK_VOYAGE_STATUS, UIConstants.BACK, UIConstants.QUIT))

        # print("1. Display Voyages")
        # print("2. Register Voyages")
        # print("3. Populate Voyage")
        # print("4. Check Voyage Status")
        # print("b. Back")
        # print("q. Quit")

    def input_prompt_voyages(self):
        # LES INPUT . <---- PUNKTUR
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

            elif command == "5" or command == "5.":
                pass

            else:
                print(UIConstants.INVALID_INPUT)