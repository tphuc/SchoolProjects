MAX_COLS = 26
MAX_ROWS = 26
COL_LABELS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class Game:
    PvP = 'PvP'
    PvC = 'PvC'

    def __init__(self, player1, player2, mode=Game.PvP, currentTurn=0):
        self.player1 = Player()
        if mode == GameMode.PvP:
            self.player2 = Bot()
        else:
            self.player2 = Player()
        self.turn = currentTurn
        self.mode = mode
        self.board = Board(MAX_COLS, MAX_ROWS)

    def save(self, filename):
        with open('save/'+filename, 'w') as f:
            f.write(self.map)

    @staticmethod
    def load(filename):
        pass

    def start(start):
        pass
    

class Board:
    def __init__(self, cols, rows):
        self.cols = min(MAX_COLS, 25)
        self.rows = min(MAX_ROWS, 25)
        self.data = self.__initData(self.cols, self.rows)

    def __initData(self, cols, rows):
        data = []
        for i in range(rows):
            data.append([])
            for j in range(cols):
                data[i].append(0)
        return data

    
    def __convertCoord(self, move):
        """ convert move(type:string) ---> type:tuple(row, col)
        - notes: Letter stand first
        ex: 'A9' --> (0, 9) # row index 0, col index 9
        """
        try:
            move = move.lower()
            row, col = int(ord(move[0]) - ord('a')), int(move[1])
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

    def update(self, row, col, val):
        """ update data[row][col] = val """
        self.data[row][col] = val


    def display(self):
        for row in data:
            print("\n".join([str(e) for e in row]))    





class Player:
    promptHelp = "\nHint: type 'pause' for pause the game"

    def __init__(self, name='player'):
        self.name = name

    def setName(self, name):
        self.name = name

    def getMove(self):
        move = input("{} turn. Enter the move: ".format(self.name) + Player.promptHelp)
        return move
    

class Bot:
    def getMove(self):
        return 'a1'
    