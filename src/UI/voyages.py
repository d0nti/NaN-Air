HEADER_VOYAGES = (
      "------------------------------"
    + "\n"
    + "  NaN Air - Manage Voyages"
    + "\n"
    + "------------------------------"
)

class Voyages:
    def __init__(self):
        self.voyages_menu_output()
        
    def voyages_menu_output(self):
        # PRENTAR MENU-IÐ .  <---- PUNKTUR
        print(HEADER_VOYAGES)
        print("1. Register Voyage")
        print("2. Edit Voyage")
        print("3. Populate Voyage")
        print("4. Display Voyages")
        print("5. Check Voyage Status")
        print("b. Back")
        print("q. Quit")

    def input_prompt_voyages(self):
        # LES INPUT . <---- PUNKTUR
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
                pass

            else:
                print("Invalid input! Please try again.")