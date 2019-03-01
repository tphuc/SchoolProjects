from gameplay import *

def hr(func):
    def _drawbound(*args, **kwargs):
        print('='*50)
        func(*args, **kwargs)
    return _drawbound


class Window:
    def __init__(self, cols=MAX_COLS, rows=MAX_ROWS):
        """ simple user-interface on terminal """
        self.draw_menu()
        """ game is not set yet ! """
        self.game = None

    @hr
    def draw_menu(self):
        """ 
        - draw menu and promt for user's choice 
        - execute command option
        """
        def prompt_user_menu():
            """ 
            - prompt user choice (menu)
            - if there was invalid choice, promt again
            """
            try:
                option = int(input("Enter your choice: "))
            except ValueError: 
                print("Invalid choice!")
                self.draw_menu()
            execute_user_option(option)

        def execute_user_option(option):
            options = { 1: self.PvP, 
                        2: self.PvC, 
                        3: self.loadGame, 
                        4: self.saveGame, 
                        5: self.history}
            func_call = options.get(option)
            func_call()
        print("\tMENU")
        print("1: PvP mode\n2: PvC mode\n3: Load game\n4: Save game\n5: History")
        prompt_user_menu()

    @hr 
    def PvP(self):
        player1name = input("enter player1 name: ")
        player2name = input("enter player2 name: ")
        Player1 = Player(player1name)
        Player2 = Player(player2name)
        self.game = Game(Player1, Player2, Mode.PvP)
        self.game.start()

    @hr
    def PvC(self):
        player1name = input("enter player name: ")
        Player1 = Player(player1name)
        BotAI = Bot("Computer")
        self.game = Game(Player1, BotAI, Mode.PvC)
        self.game.start()
    
    @hr
    def loadGame(self):
        import os
        savedFiles = os.listdir('./' + save_root)
        print("********** All saved game **********")
        [print(file) for file in savedFiles]
        fileChosen = input("which saved game you want to load? :")
        Game.loadgame(save_root + fileChosen)

    @hr
    def saveGame(self):
        fileToSave = input("File name to save: ")
        self.game.save(save_root + fileToSave)


    def history(self):
        pass

if __name__ == "__main__":
    window = Window()

