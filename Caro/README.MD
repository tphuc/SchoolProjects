CARO GAME

#########################################

FILESAVE FORMAT:
- matrix 26 x 26  # (board)
- mode  # (PvP or PvC)
- turn  # (0 or 1)
ex:
. . . . . . . . . . . . . . . . . . . .
. . . . X O . . 0 X 0 X 0 X 0 . . . . . 
... (26 x 26)
PvP
0

#########################################

`main.py` : the python file to run

`window.py`: handle user-interface

`gameplay.py`: contains 4 class

`-       Game`: game instance, when you load a game, or create a new game, you literally create an instance of this class 
`               +  newgame = Game(player1, player2,...)`

`-       Board`: the class for drawing the *board*. It can help to check
                + Is the player move is a valid move?
                + Is someone gonna win by checking the board... ?
                + Update the board by player move....
             
`-       Player`: the class controlled by `user`. It will prompt for user's input everytime it's player'turn.
           
`-       Bot`: the class controlled by `code logic`. It will not promt for user's input. It can make the move by *random* :p , *using algorithm mini-max*.

