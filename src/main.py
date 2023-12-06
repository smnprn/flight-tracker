from uihandler import *
from apihandler import *

ui = UiHandler()
api_h = ApiHandler()
#filereader = FileReader()

while True:
    user_choice = ui.starting_menu()

    if user_choice == "1":
        print(api_h.search_flight())
    elif user_choice == "2":
        pass
        #filereader.load_settings()
        #filereader.print_settings()
    elif user_choice == "3":
        ui.show_credits()
    elif user_choice == "0":
        print("Bye!")
        break
    else:
        print("Invalid input, please choose one of the following options: ")
