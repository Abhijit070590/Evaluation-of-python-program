
def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    kings = {}

    ''' Your code comes here '''
    for i in board:
        if 'k' in i:
            x=i.index('k')+1
            y=board.index(i)+1
            kings['k']=(x,y)
        if 'K' in i:
            x=i.index('K')+1
            y=board.index(i)+1
            kings['K']=(x,y)
    
            
    
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
    if(k=='k'):
        x=king_pos[0]-1
        y=king_pos[1]-1
        if(x>0 and y<7):
            if 'P' in board[x-1][y+1]:
                a=x-1
                b=y+1
                check=(k,'P',a,b)
        if(x<7 and y<7):
            if 'P' in board[x+1][y+1]:
                a=x+1
                b=y+1
                check=(k,'P',a,b)
    elif(k=='K'):
        x=king_pos[0]-1
        y=king_pos[1]-1
        if(x>0 and y<7):
            if 'p' in board[x-1][y-1]:
                a=x-1
                b=y-1
                check=(k,'p',a,b)
        if(x<7 and y<7):
            if 'p' in board[x+1][y-1]:
                a=x+1
                b=y-1
                check=(k,'P',a,b)
        
        
        
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
    if(k=='k'):
        x=king_pos[0]-1
        y=king_pos[1]-1
        if(y>1 and x>0):
            if 'N' in board[x-1][y-2] :
                a=x-1
                b=y-2
                check=(k,'N',a,b)
        if(y<1 and x<7):
            if 'N' in board[x+1][y-2]:
                a=x+1
                b=y-2
                check=(k,'N',a,b)
        if(y<6 and x>0):
            if 'N' in board[x-1][y+2]:
                a=x-1
                b=y+2
                check=(k,'N',a,b)
        if(y<6 and x<7):
            if 'N' in board[x+1][y+2]:
                a=x+1
                b=y+2
                check=(k,'N',a,b)
        if(y>0 and x>1):
            if 'N' in board[x-2][y-1]:
                a=x-2
                b=y-1
                check=(k,'N',a,b)
        if(y>0 and x<6):
            if 'N' in board[x+2][y-1]:
                a=x+2
                b=y-1
                check=(k,'N',a,b)
        if(y<7 and x>1):
            if 'N' in board[x-2][y+1]:
                a=x-2
                b=y+1
                check=(k,'N',a,b)
        if(y<7 and x<6):
            if 'N' in board[x+2][y+1]:
                a=x+2
                b=y+1
                check=(k,'N',a,b)
        
    elif(k=='K'):
        x=king_pos[0]-1
        y=king_pos[1]-1
        if(y>1 and x>0):
            if 'n' in board[x-1][y-2] :
                a=x-1
                b=y-2
                check=(k,'n',a,b)
        if(y<1 and x<7):
            if 'n' in board[x+1][y-2]:
                a=x+1
                b=y-2
                check=(k,'n',a,b)
        if(y<6 and x>0):
            if 'n' in board[x-1][y+2]:
                a=x-1
                b=y+2
                check=(k,'n',a,b)
        if(y<6 and x<7):
            if 'n' in board[x+1][y+2]:
                a=x+1
                b=y+2
                check=(k,'n',a,b)
        if(y>0 and x>1):
            if 'n' in board[x-2][y-1]:
                a=x-2
                b=y-1
                check=(k,'n',a,b)
        if(y>0 and x<6):
            if 'n' in board[x+2][y-1]:
                a=x+2
                b=y-1
                check=(k,'n',a,b)
        if(y<7 and x>1):
            if 'n' in board[x-2][y+1]:
                a=x-2
                b=y+1
                check=(k,'n',a,b)
        if(y<7 and x<6):
            if 'n' in board[x+2][y+1]:
                a=x+2
                b=y+1
                check=(k,'n',a,b)
        
        
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
    kings_position=find_kings(board)
    print kings_position
    check=check_pawn_attack(board,'k',kings_position['k'])
    if(check== None):
        check=check_knight_attack(board,'k',kings_position['k'])
    if(check==None):
        left=kings_position['k'][0]-1
        right=kings_position['k'][0]+1
        up=kings_position['k'][1]-1
        down=kings_position['k'][1]+1
        while(left>=0):
            for i in board:
                if i[left]=='R':
                    check=('k','R',board.index(i),left)
                elif i[left]=='Q':
                    check=('k','Q',board.index(i),left)
                elif i[left]!='.':
                    break
                else:
                    left-=1
        while(right<=7 and check==None):
            for i in board:
                if i[left]=='R':
                    check=('k','R',board.index(i),right)
                elif i[left]=='Q':
                    check=('k','Q',board.index(i),right)
                elif i[right]!='.':
                    break
                else:
                    right+=1
        while(up>=0 and check==None):
            for i in board:
                if i[left]=='R':
                    check=('k','R',board.index(i),up)
                elif i[left]=='Q':
                    check=('k','Q',board.index(i),up)
                elif i[up]!='.':
                    break
                else:
                    up-=1
        while(down<=7 and check==None):
            for i in board:
                if i[left]=='R':
                    check=('k','R',board.index(i),down)
                elif i[left]=='Q':
                    check=('k','Q',board.index(i),down)
                elif i[down]!='.':
                    break
                else:
                    down+=1  
    if(check== None):
        check=check_knight_attack(board,'K',kings_position['K'])
    if(check== None):
        check=check_pawn_attack(board,'K',kings_position['K'])
    if(check==None):
        left=kings_position['K'][0]-1
        right=kings_position['K'][0]+1
        up=kings_position['K'][1]-1
        down=kings_position['K'][1]+1
        while(left>=0):
            for i in board:
                if i[left]=='r':
                    check=('K','r',board.index(i),left)
                elif i[left]=='q':
                    check=('K','q',board.index(i),left)
                elif i[left]!='.':
                    break
                else:
                    left-=1
        while(right<=7 and check==None):
            for i in board:
                if i[left]=='r':
                    check=('K','r',board.index(i),right)
                elif i[left]=='q':
                    check=('K','q',board.index(i),right)
                elif i[right]!='.':
                    break
                else:
                    right+=1
        while(up>=0 and check==None):
            for i in board:
                if i[left]=='r':
                    check=('K','r',board.index(i),up)
                elif i[left]=='q':
                    check=('K','q',board.index(i),up)
                elif i[up]!='.':
                    break
                else:
                    up-=1
        while(down<=7 and check==None):
            for i in board:
                if i[left]=='r':
                    check=('K','r',board.index(i),down)
                elif i[left]=='q':
                    check=('K','q',board.index(i),down)
                elif i[down]!='.':
                    break
                else:
                    down+=1 
        
    return check
                    
if __name__ == '__main__':
    board =         [['r','n','b','q','.','b','n','r'],
                    ['p','p','p','p','p','.','.','.'],
                    ['.','.','.','.','.','.','p','.'],
                    ['.','.','.','.','.','.','.','k'],
                    ['.','.','.','.','.','Q','P','p'],
                    ['.','.','.','.','P','.','.','.'],
                    ['P','P','P','P','.','P','.','P'],
                    ['R','N','B','.','K','.','N','R']]
    check=check_check(board)
    print check