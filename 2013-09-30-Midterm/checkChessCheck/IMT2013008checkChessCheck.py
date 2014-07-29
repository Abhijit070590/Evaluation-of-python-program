
def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    kings = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j]=='k'):
                kings['k']=(i,j)
            elif(board[i][j]=='K'):
                kings['K']=(i,j)

    ''' Your code comes here '''
    
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
    x=king_pos[0]
    y=king_pos[1]
    if(k=='k'):
        attacker='P'
        if(x+1>0 and y+1>0):
            if(board[x+1][y+1]=='P'):
                check=1
                attacker_x=x+1
                attacker_y=y+1
        if(x+1>0 and y-1>0):
            if(board[x+1][y-1]=='P'):
                check=1
                attacker_x=x+1
                attacker_y=y-1
        if(x-1>0 and y+1>0):
            if(board[x-1][y+1]=='P'):
                check=1
                attacker_x=x-1
                attacker_y=y+1
        if(x+1>0 and y+1>0):
            if(board[x-1][y-1]=='P'):
                check=1
                attacker_x=x-1
                attacker_y=y-1
    if(k=='K'):
        attacker='p'
        if(x+1>0 and y+1>0):
            if(board[x+1][y+1]=='p'):
                check=1
                attacker_x=x+1
                attacker_y=y+1
        if(x+1>0 and y-1>0):
            if(board[x+1][y-1]=='p'):
                check=1
                attacker_x=x+1
                attacker_y=y-1
        if(x-1>0 and y+1>0):
            if(board[x-1][y+1]=='p'):
                check=1
                attacker_x=x-1
                attacker_y=y+1
        if(x+1>0 and y+1>0):
            if(board[x-1][y-1]=='p'):
                check=1
                attacker_x=x-1
                attacker_y=y-1
        if(check==1):
            check=(k,attacker,attacker_x,attacker_y)
                
            
        
        
            
            
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
    x=king_pos[0]
    y=king_pos[1]
    for i in range(2):
        if(k=='k'):
            attacker='N'
            if(x+1>0 and y+1>0):
                if(board[x+1][y+1]=='N'):
                    check=1
                    attacker_x=x+1
                    attacker_y=y+1
            if(x+1>0 and y-1>0):
                if(board[x+1][y-1]=='N'):
                    check=1
                    attacker_x=x+1
                    attacker_y=y-1
            if(x-1>0 and y+1>0):
                if(board[x-1][y+1]=='N'):
                    check=1
                    attacker_x=x-1
                    attacker_y=y+1
            if(x+1>0 and y+1>0):
                if(board[x-1][y-1]=='N'):
                    check=1
                    attacker_x=x-1
                    attacker_y=y-1
        if(k=='K'):
            attacker='n'
            if(x+1>0 and y+1>0):
                if(board[x+1][y+1]=='n'):
                    check=1
                    attacker_x=x+1
                    attacker_y=y+1
            if(x+1>0 and y-1>0):
                if(board[x+1][y-1]=='n'):
                    check=1
                    attacker_x=x+1
                    attacker_y=y-1
            if(x-1>0 and y+1>0):
                if(board[x-1][y+1]=='n'):
                    check=1
                    attacker_x=x-1
                    attacker_y=y+1
            if(x+1>0 and y+1>0):
                if(board[x-1][y-1]=='n'):
                    check=1
                    attacker_x=x-1
                    attacker_y=y-1
            if(check==1):
                    check=(k,attacker,attacker_x,attacker_y)
            x=x+1
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
    k='k'
    pos=find_kings(board)
    x=pos[0]
    y=pos[1]
    i=1
    while(y+i>=0 and y+i<8 ):
        if(board[x][y+i]<>'.'):
            if(board[x][y+i]=='R'):
                check=(k,'R',x,y+i)
                return check
            elif(board[x][y+i]=='Q'):
                check=(k,'R',x,y+i)
                return check
        i+=1
    while(y-i>=0 and y-i<8 ):
        if(board[x][y-i]<>'.'):
            if(board[x][y-i]=='R'):
                check=(k,'R',x,y-i)
                return check
            elif(board[x][y-i]=='Q'):
                check=(k,'R',x,y-i)
                return check
        i+=1
    while(x+i>=0 and x+i<8 ):
        if(board[x+i][y]<>'.'):
            if(board[x+i][y]=='R'):
                check=(k,'R',x+i,y)
                return check
            elif(board[x][x+i]=='Q'):
                check=(k,'R',x+i,y)
                return check
        i+=1
    while(x-i>=0 and x-i<8 ):
        if(board[x-i][y]<>'.'):
            if(board[x-i][y]=='R'):
                check=(k,'R',x-i,y)
                return check
            elif(board[x-i][y]=='Q'):
                check=(k,'R',x-i,y)
                return check
        i+=1
    
    k='K'
    pos=find_kings(board)
    x=pos[0]
    y=pos[1]
    i=1
    while(y+i>=0 and y+i<8 ):
        if(board[x][y+i]<>'.'):
            if(board[x][y+i]=='R'):
                check=(k,'R',x,y+i)
                return check
            elif(board[x][y+i]=='Q'):
                check=(k,'R',x,y+i)
                return check
        i+=1
    while(y-i>=0 and y-i<8 ):
        if(board[x][y-i]<>'.'):
            if(board[x][y-i]=='R'):
                check=(k,'R',x,y-i)
                return check
            elif(board[x][y-i]=='Q'):
                check=(k,'R',x,y-i)
                return check
        i+=1
    while(x+i>=0 and x+i<8 ):
        if(board[x+i][y]<>'.'):
            if(board[x+i][y]=='R'):
                check=(k,'R',x+i,y)
                return check
            elif(board[x][x+i]=='Q'):
                check=(k,'R',x+i,y)
                return check
        i+=1
    while(x-i>=0 and x-i<8 ):
        if(board[x-i][y]<>'.'):
            if(board[x-i][y]=='R'):
                check=(k,'R',x-i,y)
                return check
            elif(board[x-i][y]=='Q'):
                check=(k,'R',x-i,y)
                return check
        i+=1
    
    
    ''' You code comes here '''
        
    return check
                    
if __name__ == '__main__':
    pass