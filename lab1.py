import numpy as np
import random as rd


score=["PUDŁO","TRAFIONY","ZATOPIONY"]
is_end=False

def new_board():
    board = np.zeros((10, 10), dtype=int)
    ships_count=[3,2,1]
    ships_length=[2,3,4]
    directions={"up":(-1,0),"down":(1,0),"left":(0,-1),"right":(0,1)}
    k=2
    for count, ship_length in zip(ships_count, ships_length):
        placed=0
        while placed < count:
            x_localization=rd.randint(0, 9)
            y_localization=rd.randint(0, 9)
            dx, dy=directions[rd.choice(list(directions))]
            cells=[(x_localization+dx*l, y_localization+dy*l) for l in range(ship_length)]
            # cały statek musi zmieścić się na planszy i nie nachodzić na inne
            if all(0 <= x <= 9 and 0 <= y <= 9 and board[x][y] == 0 for x, y in cells):
                for x, y in cells:
                    board[x][y]=k
                k+=1
                placed+=1
    print(board)
    return board
def shoot(x,y,board):
    global is_end
    ship = board[y,x]
    if ship <= 0:
        result = score[0]
    else:
        board[y,x] = -1  # -1: trafione w pole statku
        if np.any(board == ship):
            result = score[1]
        else:
            result = score[2]
            is_end = check_end(board)
    print(result)
    return result

def check_end(board):
    return not np.any(board > 0)


board = new_board()
print(board)