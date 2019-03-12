from tkinter import *

root = Tk()
root.resizable(0,0)
WIDTH = 600
HEIGHT = 600

class BTN:
    width = 50
    height = 3

class Y:
    bot3 = HEIGHT * 7//8
    bot2 = HEIGHT * 6//8
    bot1 = HEIGHT * 5//8
    mid2 = HEIGHT * 4//8
    mid1 = HEIGHT * 3//8
    top2 = HEIGHT * 2//8
    top1 = HEIGHT * 1//8

class TickBox(Label):
    count = 0
    def __init__(self, parent, board, row, col):
        self.row = row
        self.col = col
        Label.__init__(self, parent, font=("", 10), width=2, justify="center", relief="raised", bg="#aaa")
        self.marked = False
        self.board = board
        self.bind("<Button-1>", self.mark)

    def mark(self, event):
        if not self.marked:
            if TickBox.count%2:
                self.config(text="O", fg="red")
                self.board.update_status("X") 
                self.board.list_markedO.append((self.row, self.col))
            else:
                self.config(text="X")
                self.board.update_status("O")
                self.board.list_markedX.append((self.row, self.col))
            TickBox.count += 1
            self.marked = True

        if self.board.check_endgame():
            window = Toplevel(None, width=500, height=500)
            window.wm_title("End Game!")
            Label(window, text="Congratulation!").pack(padx=30, pady=30)
            self.board.delete()


class Menu:
    def __init__(self, root):
        self.canvas = Frame(root, width=WIDTH, height=HEIGHT)
        self.title = Label(self.canvas, text="Caro game", font=("Impact",50)).pack()

        options = ["PvP", "PvC", "LoadGame", "Quit"]

        self.create_button(text=options[0], command=self.pvp)
        self.create_button(text=options[1], command=self.pvc)
        self.create_button(text=options[2], command=self.load_game)
        self.create_button(text=options[3], command=quit)

        self.canvas.pack(padx=10, pady=10)
        Frame(master=self.canvas).pack()
        
    def create_button(self, text="Not set", x=0, y=0, width=BTN.width, height=BTN.height, command=None):
        btn = Button(self.canvas, width=width,height=height, text=text,font="Impact 20",command=command).pack()
        return btn

    def create_popup(self, master, title=""):
        window = Toplevel(self.canvas)
        window.wm_title(title)
        return window
    
    def pvp(self):
        def start():
            self.canvas.forget()
            player1 = Player(name_entry1.get())
            player2 = Player(name_entry2.get())
            pop_window.destroy()
            game = Game(player1, player2, Board())
    
        pop_window = self.create_popup(self.canvas)
        Label(pop_window, text="Player1's name:", font="Impact 20").pack()
        name_entry1 = Entry(pop_window, width=10)
        name_entry1.pack()
        Label(pop_window, text="Player2's name:", font="Impact 20").pack()
        name_entry2 = Entry(pop_window, width=10)
        name_entry2.pack()
        Button(pop_window, text="Start", command=start).pack()


    def pvc(self):
        pass

    def load_game(self):
        pass

    def save_game(self):
        pass


class Game():
    def __init__(self, player1=None, player2=None, board=None):
        self.player1 = player1
        self.player2 = player2
        self.board = board


class Player():
    def __init__(self, name="player", label=None):
        self.name = name
        self.label = label


class Board:
    def __init__(self, map_data=None):
        self.status = Label(width=10, text="Turn: ",font="Impact 15", justify="center")
        self.status.grid(row=0, columnspan=5, sticky=W+E)
        # [(0, 2), (12, 9), ...]
        # (0, 2) => row-index 0, col-index 2
        # We stored 2 list of marked tickbox by its own label
        self.list_markedX = [] 
        self.list_markedO = []

        if not map_data:
            self.board = self._init_map()
        else:
            self.board = map_data

    def _init_map(self):
        board = []
        for i in range(1,26):
            row = []
            for j in range(25):
                box = TickBox(parent=None, board=self, row=i, col=j)
                box.grid(row=i, column=j)
                row.append(box)
            board.append(row)
        return board
    
    def update_status(self, turn):
        self.status.config(text="Next turn: " + turn)
    
    def check_endgame(self):
        possible_directs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)] # Unit vectors

        def normalize(vec):
            dy, dx = vec
            if dy:
                dy /= abs(dy)
            if vec[1]:
                dx /= abs(dx)
            return dy, dx

        def check_endgame(marked_ls):
            if marked_ls:
                (y1, x1) = marked_ls[0]
                for (y2, x2) in marked_ls[1:]:
                    count = 0
                    dy, dx = normalize((y2 - y1, x2 - x1)) # find the vector from 1 -> 2. Convert to unit
                    if (dy, dx) not in possible_directs:
                        continue
                    y, x = y1, x1
                    for i in range(4):
                        y, x = y + dy, x + dx
                        if (y, x) not in marked_ls:
                            break
                        count += 1
                    if count == 2:
                        return True
            return False
        
        if check_endgame(self.list_markedO) or check_endgame(self.list_markedX):
            return True

    def delete(self):
        for ls in self.board:
            for tickbox in ls:
                ls.destroy()
        self.status.destroy()


menu = Menu(root)
root.mainloop()
