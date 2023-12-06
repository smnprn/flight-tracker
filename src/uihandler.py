
class UiHandler:
    def starting_menu(self):
        print("""
            Welcome to Flight Scanner!
            Choose an option:
            1) Start scanning
            2) Settings
            3) Credits
            0) Exit
            """)
        
        choice = input("=> ")

        return choice
        
    def show_credits(self):
        print("""
            Simone Perna - 2023
            simoneperna8@gmail.com
        """)