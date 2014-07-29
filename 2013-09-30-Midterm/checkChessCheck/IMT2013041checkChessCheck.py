
def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    kings = {}
   

    ''' Your code comes here '''
    pos_k = (0,0)
    pos_K = (0,0)
    loc_x_k = 0
    loc_y_k = 0
    loc_x_K = 0
    loc_y_K = 0
    
    for i in board:
        loc_y_k = 0
        for j in i:
            if j == 'k':
                pos_k = (loc_x_k,loc_y_k)
            loc_y_k+=1
        loc_x_k+=1
        
    for a in board:
        loc_y_K = 0
        for b in a:
            if b == 'K':
                pos_K = (loc_x_K,loc_y_K)
            loc_y_K+=1
        loc_x_K+=1
        
    
    kings['k'] = pos_k
    kings['K'] = pos_K            
    
    return kings

def check_pawn_attack(board, k, king_pos):
    '''
    Check if the king (argument k - it is 'k' if it is black king and 'K' for white king) at position king_pos
    - king_pos is a tuple (row, col) - is being attacked by a opposite color pawn
    black king -- check positions (1, +/- 1) away from king_pos and see if any of them is a white pawn
    white king -- check positions (-1, +/- 1) away from king_pos and see if any of them is a black pawn
    You need to of course first check that these are legal board positions
    Return a tuple (k, attacker, attacker_x, attacker_y) - attacker will be 'P' or 'p' depending on
    whether k is 'k' or 'K' - if the king is under check, else return None
    '''
    check = None
    
    ''' You code comes here '''
    if k == 'k':
        loc_x_k = king_pos[0]
        loc_y_k = king_pos[1]
        if loc_y_k + 1 < 8:
            if loc_x_k +1 < 8:
                if board[loc_x_k + 1][loc_y_k +1] == 'P':
                    check = ('k','P', loc_x_k +1, loc_y_k+1)
            if loc_x_k -1 > -1:
                if board[loc_x_k - 1][loc_y_k +1] == 'P':
                    check = ('k','P', loc_x_k -1, loc_y_k +1)
        else:
            check = None
        
    if k == 'K':
        loc_x_K = king_pos[0]
        loc_y_K = king_pos[1]
        if loc_y_K - 1 > -1:
            if loc_x_K +1 < 8:
                if board[loc_x_K + 1][loc_y_K -1] == 'p':
                    check = ('K','p', loc_x_K +1, loc_y_K-1)
            if loc_x_K -1 > -1:
                if board[loc_x_K - 1][loc_y_K -1] == 'p':
                    check = ('K','p', loc_x_K -1, loc_y_K -1)
        else:
            check = None
        
    return check


def check_knight_attack(board, k, king_pos):
    '''
    Check if the king (argument k - it is 'k' if it is black king and 'K' for white king) at position king_pos
    - king_pos is a tuple (row, col) - is being attacked by a opposite color knight
    check positions (+/- 1, +/- 2), (+/- 2, +/- 1) away from king_pos and see if any of them is a opposite color knight
    You need to of course first check that these are legal board positions
    Return a tuple (k, attacker, attacker_x, attacker_y) - attacker will be 'N' or 'n' depending on
    whether k is 'k' or 'K' - if the king is under check, else return None
    '''
    check = None
    
    ''' You code comes here '''
    loc_x=king_pos[0]
    loc_y=king_pos[1]
    m1 = [2,-2]
    m2 = [1,-1]
    if k == 'k':
        for i in m1:
            for j in m2:
                if loc_x+i <8 and loc_y+j < 8 and loc_x + i > -1 and loc_y + j >-1:
                    if board[loc_x+i][loc_y+j]=='N':
                        check = ('k','N',loc_x+i, loc_y+j)
                            
        for i in m2:
            for j in m1:
                if loc_x+i <8 and loc_y+j < 8 and loc_x + i > -1 and loc_y + j >-1:
                    if board[loc_x+i][loc_y+j]=='N':
                        check = ('k','N',loc_x+i, loc_y+j)
    elif k == 'K':
        for i in m1:
            for j in m2:
                if loc_x+i <8 and loc_y+j < 8 and loc_x + i > -1 and loc_y + j >-1:
                    if board[loc_x+i][loc_y+j]=='n':
                        check = ('K','n',loc_x+i, loc_y+j)
                            
        for i in m2:
            for j in m1:
                if loc_x+i <8 and loc_y+j < 8 and loc_x + i > -1 and loc_y + j >-1:
                    if board[loc_x+i][loc_y+j]=='n':
                        check = ('K','n',loc_x+i, loc_y+j)
    else:
        check = None      
    return check


def check_check(board):
    '''
    Check if the black or the white king on the board is being attacked by a opposite color piece
    Find the position of the kings. For each color king
    1. Check if it is being attacked by an opposite color pawn
    2. Check if it is being attacked by an opposite color knight
    3. Try Moving in directions (0,1), (0,-1), (1,0), (-1,0) from the king_position and check if the first non-blank
    square is occupied by an opposite color Rook or Queen
    4. Try Moving in directions (1,1), (1,-1), (-1,1), (-1,-1) from the king_position and check if the first non-blank
    square is occupied by an opposite color Bishop or Queen
    You need to of course first check that these are legal board positions
    Return a tuple (k, attacker, attacker_x, attacker_y) if a king is under check - else return None
    '''
    check = None
    
    ''' You code comes here '''
    flag = 0
    
    king_dict = find_kings(board)
    if check_knight_attack(board,'k',king_dict['k']) != None:
        check = check_knight_attack(board,'k',king_dict['k'])
        return check
        flag = 1
    elif check_knight_attack(board,'K',king_dict['K']) != None:
        check = check_knight_attack(board,'K',king_dict['K'])
        return check
        flag = 1
    elif check_pawn_attack(board,'k',king_dict['k']) != None:
        check = check_pawn_attack(board,'k',king_dict['k'])
        flag = 1
        return check
    elif check_pawn_attack(board,'K',king_dict['K']) != None:
        check = check_pawn_attack(board,'K',king_dict['K'])
        flag = 1
        return check
    else:
        pos_k_x = king_dict['k'][0]
        pos_k_y = king_dict['k'][1]
        pos_K_x = king_dict['K'][0]
        pos_K_y = king_dict['K'][1]
    
        for i in range (0,8):
            if board[i][pos_k_y] == 'R':
                check = ('k','R',i,pos_k_y)
                return check
                flag = 1
            if board[i][pos_k_y] == 'Q':
                check = ('k','Q',i,pos_k_y)
                return check
                flag = 1
        for j in range (0,8):
            if board[pos_k_x][j] == 'R':
                check = ('k','R',pos_k_x,j)
                return check
                flag = 1
            if board[pos_k_x][j] == 'Q':
                check = ('k','Q',pos_k_x,j)
                return check
                flag = 1
            
        for i in range (0,8):
            if board[i][pos_K_y] == 'r':
                check = ('K','r',i,pos_K_y)
                return check
                flag = 1
            if board[i][pos_K_y] == 'q':
                check = ('K','q',i,pos_K_y)
                return check
                flag = 1
        for j in range (0,8):
            if board[pos_K_x][j] == 'r':
                check = ('K','r',pos_K_x,j)
                return check
                flag = 1
            if board[pos_K_x][j] == 'q':
                check = ('K','q',pos_K_x,j)
                return check
                flag = 1
            
        tempx=pos_k_x
        tempy=pos_k_y
    
        while tempx<8 and tempy<8:
            if board[tempx][tempy] == 'Q':
                check = ('k','Q',tempx,tempy)
                return check
                flag = 1
            if board[tempx][tempy] == 'B':
                check = ('k','B',tempx,tempy)
                flag = 1
                return check
            tempx+=1
            tempy+=1
            
        tempx=pos_k_x
        tempy=pos_k_y
        
        while tempx<8 and tempy>-1:
            if board[tempx][tempy] == 'Q':
                check = ('k','Q',tempx,tempy)
                return check
                flag = 1
            if board[tempx][tempy] == 'B':
                check = ('k','B',tempx,tempy)
                return check
                flag = 1
            tempx+=1
            tempy-=1
        
        tempx=pos_k_x
        tempy=pos_k_y
    
        while tempx>-1 and tempy<8:
            if board[tempx][tempy] == 'Q':
                check = ('k','Q',tempx,tempy)
                return check
                flag = 1
            if board[tempx][tempy] == 'B':
                check = ('k','B',tempx,tempy)
                return check
                flag = 1
            tempx-=1
            tempy+=1
    
        tempx=pos_k_x
        tempy=pos_k_y
    
        while tempx>-1 and tempy>-1:
            if board[tempx][tempy] == 'Q':
                check = ('k','Q',tempx,tempy)
                return check
                flag = 1
            if board[tempx][tempy] == 'B':
                check = ('k','B',tempx,tempy)
                return check
                flag = 1
            tempx-=1
            tempy-=1
    
        tempx=pos_K_x
        tempy=pos_K_y
    
        while tempx<8 and tempy<8:
            if board[tempx][tempy] == 'q':
                check = ('K','q',tempx,tempy)
                return check
                flag = 1
            if board[tempx][tempy] == 'b':
                check = ('K','b',tempx,tempy)
                return check
                flag = 1
            tempx+=1
            tempy+=1
            
        tempx=pos_K_x
        tempy=pos_K_y
    
        while tempx<8 and tempy>-1:
            if board[tempx][tempy] == 'q':
                check = ('K','q',tempx,tempy)
                return check
                flag = 1
            if board[tempx][tempy] == 'b':
                check = ('K','b',tempx,tempy)
                return check
                flag = 1
            tempx+=1
            tempy-=1
    
        tempx=pos_K_x
        tempy=pos_K_y
    
        while tempx>-1 and tempy<8:
            if board[tempx][tempy] == 'q':
                check = ('K','q',tempx,tempy)
                return check
                flag = 1
            if board[tempx][tempy] == 'b':
                check = ('K','b',tempx,tempy)
                return check
                flag = 1
            tempx-=1
            tempy+=1
    
        tempx=pos_K_x
        tempy=pos_K_y
    
        while tempx>-1 and tempy>-1:
            if board[tempx][tempy] == 'q':
                check = ('K','q',tempx,tempy)
                return check
                flag = 1
            if board[tempx][tempy] == 'B':
                check = ('K','b',tempx,tempy)
                return check
                flag = 1
            tempx-=1
            tempy-=1
        
    if flag == 0:
        return check
                    
if __name__ == '__main__':
    pass