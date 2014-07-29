
def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    #kings = {}
    kings={'k':(0,0),'K':(0,0)}
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=='k':
                kings['k']=(i,j)
            elif board[i][j]=='K':
                kings['K']=(i,j)
    
    
    
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
    w=0
    ''' You code comes here '''
    if k in range(97,122):
        w+=1 
        
    if check_pos(king_pos):
        return check
        
    if w:
        if not check_pos((king_pos[0]-1,king_pos[1]+1)):
            if board[king_pos[0]-1][king_pos[1]+1]=='p':
                check=(k,'p',king_pos[0]-1,king_pos[1]+1)
        if not check_pos((king_pos[0]-1,king_pos[1]-1)):
            if board[king_pos[0]-1][king_pos[1]-1]=='p':
                check=(k,'p',king_pos[0]-1,king_pos[1]-1)
            
    else:
        if not check_pos((king_pos[0]+1,king_pos[1]+1)):        
            if board[king_pos[0]+1][king_pos[1]+1]=='P':
                check=(k,'P',king_pos[0]+1,king_pos[1]+1)
        if not check_pos((king_pos[0]+1,king_pos[1]-1)):
            if board[king_pos[0]+1][king_pos[1]-1]=='P':
                check=(k,'P',king_pos[0]+1,king_pos[1]-1)
        
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
    w=[]
    op=''
    
    if k in range(97,122):
        w+=1 
        
    if check_pos(king_pos):
        return check
    
    if w:
        op='n'
    else:
        op='N'
    
    if board[king_pos[0]+1][king_pos[1]+2]==op and check_pos((king_pos[0]+1,king_pos[1]+2))==1:
        check=(k,op,king_pos[0]+1,king_pos[1]+2)
    if board[king_pos[0]-1][king_pos[1]+2]==op and not check_pos((king_pos[0]-1,king_pos[1]+2)):
        check=(k,op,king_pos[0]-1,king_pos[1]+2)
    if board[king_pos[0]+1][king_pos[1]-2]==op and not check_pos((king_pos[0]+1,king_pos[1]-2)):
        check=(k,op,king_pos[0]+1,king_pos[1]-2)
    if board[king_pos[0]-1][king_pos[1]-2]==op and not check_pos((king_pos[0]-1,king_pos[1]+-2)):
        check=(k,op,king_pos[0]-1,king_pos[1]-2)
    if board[king_pos[0]+2][king_pos[1]+1]==op and not check_pos((king_pos[0]+2,king_pos[1]+1)):
        check=(k,op,king_pos[0]+2,king_pos[1]+1)        
    if board[king_pos[0]-2][king_pos[1]+1]==op and not check_pos((king_pos[0]-2,king_pos[1]+1)):
        check=(k,op,king_pos[0]-2,king_pos[1]+1)
    if board[king_pos[0]+2][king_pos[1]-1]==op and not check_pos((king_pos[0]+2,king_pos[1]-1)):
        check=(k,op,king_pos[0]+2,king_pos[1]-1)
    if board[king_pos[0]-2][king_pos[1]-1]==op and not check_pos((king_pos[0]-2,king_pos[1]-1)):
        check=(k,op,king_pos[0]-2,king_pos[1]-1)                  
    
    return check

def check_pos(king_pos):
    if king_pos[0]>7 or king_pos[0]<0 or king_pos[1]>7 or king_pos[1]<0:
        return 1

def check_rook_queen_attack(board, k, king_pos):
    check = None
    
    if check_pos(king_pos):
        return check
    
    w=[]
    
    if k in range(97,122):
        w+=1 
    
    if w:
        lop=['r','q']
    else:
        lop=['R','Q']
    i=0    
    while(board[king_pos[0]][king_pos[1]+i]!='.'):
        i+=1
    if board[king_pos[0]][king_pos[1]+i] in lop:
        check=(k,board[king_pos[0]][king_pos[1]+i],king_pos[0],king_pos[1]+i)
    
    i=0    
    while(board[king_pos[0]][king_pos[1]-i]!='.'):
        i+=1
    if board[king_pos[0]][king_pos[1]-i] in lop:
        check=(k,board[king_pos[0]][king_pos[1]-i],king_pos[0],king_pos[1]-i)
        
    i=0    
    while(board[king_pos[0]+i][king_pos[1]]!='.'):
        i+=1
    if board[king_pos[0]+i][king_pos[1]] in lop:
        check=(k,board[king_pos[0]+i][king_pos[1]],king_pos[0]+i,king_pos[1])
    
    i=0    
    while(board[king_pos[0]-i][king_pos[1]]!='.'):
        i+=1
    if board[king_pos[0]-i][king_pos[1]] in lop:
        check=(k,board[king_pos[0]-i][king_pos[1]],king_pos[0]-i,king_pos[1])
    
    return check
    

def check_bishop_queen_attack(board,k,king_pos):
    check = None
    if check_pos(king_pos):
        return check 
    w=[]
    
    if k in range(97,122):
        w+=1 
    
    if w:
        lop=['b','q']
    else:
        lop=['B','Q']
    
    i=0
    while(board[king_pos[0]+i][king_pos[1]+i]!='.'):
        i+=1
    if board[king_pos[0]+i][king_pos[1]+i] in lop:
        check=(k,board[king_pos[0]+i][king_pos[1]+i],king_pos[0]+i,king_pos[1]+i)
    i=0
    while(board[king_pos[0]+i][king_pos[1]-i]!='.'):
        i+=1
    if board[king_pos[0]+i][king_pos[1]-i] in lop:
        check=(k,board[king_pos[0]+i][king_pos[1]-i],king_pos[0]+i,king_pos[1]-i)
    i=0
    while(board[king_pos[0]-i][king_pos[1]+i]!='.'):
        i+=1
    if board[king_pos[0]-i][king_pos[1]+i] in lop:
        check=(k,board[king_pos[0]-i][king_pos[1]+i],king_pos[0]-i,king_pos[1]+i)
    i=0
    while(board[king_pos[0]-i][king_pos[1]-i]!='.'):
        i+=1
    if board[king_pos[0]-i][king_pos[1]-i] in lop:
        check=(k,board[king_pos[0]-i][king_pos[1]-i],king_pos[0]-i,king_pos[1]-i)

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

    kings=find_kings(board)
    check=check_pawn_attack(board, 'K',kings['K'])
    if not check: check=check_knight_attack(board, 'K', kings['K'])
    if not check: check=check_rook_queen_attack(board,'K',kings['K'])
    if not check: check=check_bishop_queen_attack(board,'K',kings['K'])  
    if not check: check=check_pawn_attack(board, 'k',kings['k'])  
    if not check: check=check_knight_attack(board, 'k', kings['k'])
    if not check: check=check_rook_queen_attack(board,'k',kings['k'])
    if not check:check=check_bishop_queen_attack(board,'k',kings['k'])        
    return check
                    
if __name__ == '__main__':
    pass