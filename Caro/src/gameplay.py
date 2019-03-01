MAX_COLS = 26
MAX_ROWS = 26
COL_LABELS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

save_root = 'save/'
history_root = 'history/'


class Mode:
    PvP = 'PvP'
    PvC = 'PvC'

class Game:
    def __init__(self, player1, player2, mode, currentTurn=0):
        self.player1 = player1
        self.player2 = player2
        self.turn = currentTurn
        self.mode = mode
        self.board = Board(MAX_COLS, MAX_ROWS)

    def save(self, filename):
        with open(save_root+filename, 'w') as f:
            f.write(self.map)

    @staticmethod
    def load(filename):
        pass

    def start(self):
        while not self.board.isEndGame():
            self.board.display()

            # Check the turn and set turn for nextplayer
            if self.turn == 0:
                nextplayer = self.player1
                mark = 'X'
                self.turn = 1
            else:
                nextplayer = self.player2
                mark = 'O'
                self.turn = 0
    
            move = nextplayer.getMove()
            while not self.board.isValidOnBoard(move):
                print("not a valid move!")
                move = nextplayer.getMove()
            self.board.update(move, mark)

        pass
    

class Board:
    def __init__(self, cols, rows):
        self.cols = min(MAX_COLS, cols)
        self.rows = min(MAX_ROWS, rows)
        self.data = self.__initData(self.cols, self.rows)

    def __initData(self, cols, rows):
        data = []
        for i in range(rows):
            data.append([])
            for j in range(cols):
                data[i].append(".")
        return data

    
    def __convertCoord(self, move):
        """ convert move(type:string) ---> type:tuple(row, col)
        - notes: Letter stand first
        ex: 'A9' --> (0, 9) # row index 0, col index 9
        """
        try:
            move = move.lower()
            row, col = int(ord(move[0]) - ord('a')), int(move[1:])
        except:
            return False
        return row, col


    def isValidOnBoard(self, move):
        """ check if user move is a valid move """
        try:
            rows, cols = self.__convertCoord(move)
            return 0 <= rows <= MAX_COLS and 0 <= cols <= MAX_COLS
        except:
            print(move + 'is not a valid move !')
            return False

    def isEndGame(self):
        """ code here """
        return False

    def update(self, move, mark):
        def __update(row, col, val):
            """ update data[row][col] = val """
            self.data[row][col-1] = val
        row, col = self.__convertCoord(move)
        __update(row, col, mark)

        


    def display(self):
        """ print the board """
        print(" ", end="")
        [print('{:3d}'.format(i), end="") for i in range(1, 27)]
        print("")
        for i in range(len(self.data)):
            print( '{0:3s}'.format(chr(ord('a') + i)), end="")
            print("  ".join(self.data[i]), end="\n")
    
    





class Player:
    promptHelp = "\nHint: type 'pause' for pause the game"

    def __init__(self, name='player'):
        self.name = name

    def setName(self, name):
        self.name = name

    def getMove(self):
        move = input("{} turn. Enter the move: ".format(self.name))
        return move
    

class Bot:
    def getMove(self):
        return 'a1'
    