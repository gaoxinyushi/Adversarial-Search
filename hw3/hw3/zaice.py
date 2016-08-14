import gamePlay
from copy import deepcopy
from getAllPossibleMoves import getAllPossibleMoves


alpha = -9999
beta = 9999

def evaluation(board, color):

    
    opponentColor = gamePlay.getOpponentColor(color)
    
    value = 0
    for piece in range(1, 33):
        xy = gamePlay.serialToGrid(piece)
        x = xy[0]
        y = xy[1]
                
        if board[x][y].upper() == color.upper():
            value = value + 1
        elif board[x][y].upper() == opponentColor.upper():
            value = value - 1
    
    return value


def max_value(board,color,depth):
    global alpha,beta
    if depth == 0: 
        return evaluation(board,color)
    depth-=1
    value=-9999
    moves = getAllPossibleMoves(board, color)
    if len(moves) == 0:
        return evaluation(board,color)
    for i in moves:
        newBoard=deepcopy(board)
        gamePlay.doMove(newBoard,i)
        value = max(value,min_value(newBoard,gamePlay.getOpponentColor(color),depth)) 
        if value>=beta:
            return value
        alpha = max(alpha,value)
    return value

def min_value(board,color,depth):
    global alpha,beta
    if depth == 0:
        return evaluation(board,color)
    depth-=1
    value= 9999
    moves = getAllPossibleMoves(board, color)
    if len(moves) == 0:
        return evaluation(board,color)
    for i in moves:
        newBoard=deepcopy(board)
        gamePlay.doMove(newBoard,i)
        value = min(value,max_value(newBoard,gamePlay.getOpponentColor(color),depth)) 
        if value<=alpha:
            return value
        beta = min(beta,value)
    return value       


def nextMove(board,color,time,movesRemaining):
    moves = getAllPossibleMoves(board, color)
    if len(moves)==0:
        return "PASS"
    best_value = None
    best_move=(0,0)
    for move in moves:
        newBoard=deepcopy(board)
        gamePlay.doMove(newBoard,move)
        value = min_value(newBoard, gamePlay.getOpponentColor(color),5) 
        if value >best_value or best_value== None:
            best_value = value
            best_move = move
    return best_move




                    
        
    
     
    


    
        

