import gamePlay
from copy import deepcopy
from getAllPossibleMoves import getAllPossibleMoves
from getAllPossibleMoves import getAllPossibleMovesAtPosition

# My strategy of handling time is that using different depths. I define a function called get_depth to get the depth of searching based on time.

def evaluation(board, color):# the evaluation function is the weight of pieces to help players win 
    # Evaluation function 
    # Count the number of possible moves I have than the opponent
    # my evaluation function will take time to get possible moves
    opponentColor = gamePlay.getOpponentColor(color)
    
    value = 0
    # Loop through all board positions
    for piece in range(1, 33):
        xy = gamePlay.serialToGrid(piece)
        x = xy[0]
        y = xy[1]
                
        if board[x][y].upper() == color.upper():                   
            moves = getAllPossibleMovesAtPosition(board, x, y)           
            value = value + len(moves[0])
        elif board[x][y].upper() == opponentColor.upper():
            moves = getAllPossibleMovesAtPosition(board, x, y)  
            value = value - len(moves[0])
    
    return value


def max_value(board,color,depth,alpha,beta):# get the max value
    #alpha=-999999
    #beta=999999
    if depth == 0: #whether the depth is zero
        return evaluation(board,color)
    depth-=1
    value=-999999
    moves = getAllPossibleMoves(board, color)
    opponentColor = gamePlay.getOpponentColor(color)
    if len(moves) == 0:#whether there are available moving choices.
        return evaluation(board,color)
    for move in moves:
        newBoard=deepcopy(board)
        gamePlay.doMove(newBoard,move)
        value = max(value,min_value(newBoard,opponentColor,depth,alpha,beta)) # return the max value
        if value>=beta:#this is the Alpha-beta pruning
            return value
        alpha = max(alpha,value)
    return value

def min_value(board,color,depth,alpha,beta):#get the min value
    #alpha=-999999
    #beta=999999
    if depth == 0:# whether the depth is zero
        return evaluation(board,color)
    depth-=1
    value= 999999
    moves = getAllPossibleMoves(board, color)
    opponentColor = gamePlay.getOpponentColor(color)
    if len(moves) == 0:# whether there are available moves
        return evaluation(board,color)
    for move in moves:
        newBoard=deepcopy(board)
        gamePlay.doMove(newBoard,move)
        value = min(value,max_value(newBoard,opponentColor,depth,alpha,beta)) # return the min value
        if value<=alpha:#this is the Alpha-beta pruning
            return value
        beta = min(beta,value)
    return value       

def get_depth(time): #how I handle time to get better performance
   # global depth
    if time > 20:
        depth = 5
    if time <= 20 and time > 5:
        depth = 3
    if time <= 5:
        depth = 1
    return depth


def alpha_beta(board,color,time):
    alpha=-999999
    beta=999999
    moves = getAllPossibleMoves(board, color)
    d=get_depth(time)
    opponentColor = gamePlay.getOpponentColor(color)
    best_value = -999999
    best_move=(0,0)
    for move in moves:
        newBoard=deepcopy(board)
        gamePlay.doMove(newBoard,move)
        value = max_value(newBoard,opponentColor,d,alpha,beta) # define the depth as d considering the running time.
        if value >=best_value:
            best_value = value
            best_move = move
    return best_move


def nextMove(board, color, time, movesRemaining):
    return alpha_beta(board,color,time)

                    
        
    
     
    


    
        
