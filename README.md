# Adversarial-Search
Minimax with Alpha-Beta Pruning
For this part you will write python code for Checkers, using minimax with alpha-beta pruning, and developing a reasonable evaluation function.  Your submission will contain a procedure named nextMove which take 4 arguments, as follows:
o    Board state. This is a nested list which represents the state of the board. Initially the Board state is as follows:
[
[' ', 'r', ' ', 'r', ' ', 'r', ' ', 'r'],
['r', ' ', 'r', ' ', 'r', ' ', 'r', ' '],
[' ', 'r', ' ', 'r', ' ', 'r', ' ', 'r'],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['w', ' ', 'w', ' ', 'w', ' ', 'w', '.'],
[' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w'],
['w', ' ', 'w', ' ', 'w', ' ', 'w', ' ']
]
Cells are numbered 1 to 32 as shown in this image.
You will notice that half of the squares on board are never used. A move (in this case for for a red coin) can be defined by a pair such as [10,15]. In this case red coin moves from 10 to 15. A move having multiple jumps can be defined by an iinput such as [10, 19, 28], where a coin at 10 jumps over coin at 15 to land on 19, and then jumps over coin at 24 to land on 28, thus removing coin at 15 and 24 from the board.
o    Color: is either the string "r" or the string "w", representing the color to play. 'r' and 'w' are the Men while 'R' and 'W' are the King. A piece becomes a king if it reaches the far end of the board.
