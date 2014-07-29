def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    kings = {}

    ''' Your code comes here '''
    row=0
    pos=0
    for row in range (0,8):
        for pos in range (0,8):
            if board[row][pos]== 'k':
                kings[board[row][pos]]= (row,pos)
            if board[row][pos]=='K':
                kings[board[row][pos]]= (row,pos)
            pos+=1
        row+=1
                
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
    
    if k=='k':
        if board[king_pos[0]+1][king_pos[1]+1]=='P':
            check = (k,'P', king_pos[0]+1,king_pos[1]+1)
        
        if board[king_pos[0]+1][king_pos[1]-1]=='P':
            check = (k,'P', king_pos[0]+1,king_pos[1]-1)
            
    else:
        if board[king_pos[0]-1][king_pos[1]+1]=='p':
            check = (k,'p', king_pos[0]+1,king_pos[1]+1)
        
        if board[king_pos[0]-1][king_pos[1]-1]=='p':
            check = (k,'p', king_pos[0]+1,king_pos[1]-1)
            
        
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
    
    if k=='k':
        if board[king_pos[0]+2][king_pos[1]+1]=='N':
            check = (k,'N', king_pos[0]+2,king_pos[1]+1)
        
        elif board[king_pos[0]+2][king_pos[1]-1]=='N':
            check = (k,'N', king_pos[0]+2,king_pos[1]-1)
            
        elif board[king_pos[0]-2][king_pos[1]+1]=='N':
            check = (k,'N', king_pos[0]-2,king_pos[1]+1)
            
        elif board[king_pos[0]-2][king_pos[1]-1]=='N':
            check = (k,'N', king_pos[0]-2,king_pos[1]-1)
            
    else:
        if board[king_pos[0]+2][king_pos[1]+1]=='n':
            check = (k,'n', king_pos[0]+2,king_pos[1]+1)
        
        elif board[king_pos[0]+2][king_pos[1]-1]=='n':
            check = (k,'n', king_pos[0]+2,king_pos[1]-1)
            
        elif board[king_pos[0]-2][king_pos[1]+1]=='n':
            check = (k,'n', king_pos[0]-2,king_pos[1]+1)
            
        elif board[king_pos[0]-2][king_pos[1]-1]=='n':
            check = (k,'n', king_pos[0]-2,king_pos[1]-1)
        
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
    
    king_pos=find_kings(board)
    check=check_pawn_attack(board,'k',king_pos)
    if check!= None:
        return check
    check=check_pawn_attack(board,'K',king_pos)
    if check!= None:
        return check
    check=check_knight_attack(board,'k',king_pos)
    if check!= None:
        return check
    check=check_knight_attack(board,'K',king_pos)
    if check!= None:
        return check
    
    k='k'
    pos1=king_pos[k][0]
    pos2=king_pos[k][1]  
        
    while pos2<=7:
            pos2+=1
            if (board[pos1][pos2]!='.' and (board[pos1][pos2]=='R' or board[pos1][pos2]=='Q')):
                check=(k,board[pos1][pos2],pos1,pos2)
                break
    pos2=king_pos[k][1]
    
    if check!= None:
        return check
    
    while pos2>=0:
            pos2-=1
            if (board[pos1][pos2]!='.' and (board[pos1][pos2]=='R' or board[pos1][pos2]=='Q')):
                check=(k,board[pos1][pos2],pos1,pos2)
                break
    pos2=king_pos[k][1]
    
    if check!= None:
        return check
    
    while pos1<=7:
            pos1+=1
            if (board[pos1][pos2]!='.' and (board[pos1][pos2]=='R' or board[pos1][pos2]=='Q')):
                check=(k,board[pos1][pos2],pos1,pos2)
                break
    pos1=king_pos[k][0]
    
    if check!= None:
        return check
    
    while pos1>=0:
            pos1-=1
            if (board[pos1][pos2]!='.' and (board[pos1][pos2]=='R' or board[pos1][pos2]=='Q')):
                check=(k,board[pos1][pos2],pos1,pos2)
                break
    if check!= None:
        return check
            
    k='K'
    pos1=king_pos[k][0]
    pos2=king_pos[k][1]    
        
    while pos2<=7:
            pos2+=1
            if (board[pos1][pos2]!='.' and (board[pos1][pos2]=='r' or board[pos1][pos2]=='q')):
                check=(k,board[pos1][pos2],pos1,pos2)
                break
    pos2=king_pos[k][1]
    
    if check!= None:
        return check
    
    while pos2>=0:
            pos2-=1
            if (board[pos1][pos2]!='.' and (board[pos1][pos2]=='r' or board[pos1][pos2]=='q')):
                check=(k,board[pos1][pos2],pos1,pos2)
                break
    pos2=king_pos[k][1]
    
    if check!= None:
        return check
    
    while pos1<=7:
            pos1+=1
            if (board[pos1][pos2]!='.' and (board[pos1][pos2]=='r' or board[pos1][pos2]=='q')):
                check=(k,board[pos1][pos2],pos1,pos2)
                break
    pos1=king_pos[k][0]
    
    if check!= None:
        return check
    
    while pos1>=0:
            pos1-=1
            if (board[pos1][pos2]!='.' and (board[pos1][pos2]=='r' or board[pos1][pos2]=='q')):
                check=(k,board[pos1][pos2],pos1,pos2)
                break
    if check!= None:
        return check
    
    k='k'
    pos1=king_pos[k][0]
    pos2=king_pos[k][1] 
    
    while pos1>=0 and pos2>=0:
        pos1-=1
        pos2-=1
        if (board[pos1][pos2]!='.' and (board[pos1][pos2]=='B' or board[pos1][pos2]=='Q')):
                check=(k,board[pos1][pos2],pos1,pos2)
                break
    if check!= None:
        return check
    
    pos1=king_pos[k][0]
    pos2=king_pos[k][1]  
    
    while pos1>=0 and pos2<=7:
        pos1-=1
        pos2+=1
        if (board[pos1][pos2]!='.' and (board[pos1][pos2]=='B' or board[pos1][pos2]=='Q')):
                check=(k,board[pos1][pos2],pos1,pos2)
                break
    if check!= None:
        return check
    
    pos1=king_pos[k][0]
    pos2=king_pos[k][1]  
    
    while pos1<=7 and pos2<=7:
        pos1+=1
        pos2+=1
        if (board[pos1][pos2]!='.' and (board[pos1][pos2]=='B' or board[pos1][pos2]=='Q')):
                check=(k,board[pos1][pos2],pos1,pos2)
                break
    if check!= None:
        return check
    
    pos1=king_pos[k][0]
    pos2=king_pos[k][1]  
    
    while pos1>=0 and pos2<=7:
        pos1-=1
        pos2+=1
        if (board[pos1][pos2]!='.' and (board[pos1][pos2]=='B' or board[pos1][pos2]=='Q')):
                check=(k,board[pos1][pos2],pos1,pos2)
                break
            
    if check!= None:
        return check
            
    pos1=king_pos[k][0]
    pos2=king_pos[k][1] 
    
    k='K'
    pos1=king_pos[k][0]
    pos2=king_pos[k][1] 
    
    while pos1>=0 and pos2>=0:
        pos1-=1
        pos2-=1
        if (board[pos1][pos2]!='.' and (board[pos1][pos2]=='b' or board[pos1][pos2]=='q')):
                check=(k,board[pos1][pos2],pos1,pos2)
                break
    pos1=king_pos[k][0]
    pos2=king_pos[k][1] 
    
    if check!= None:
        return check
    
    while pos1>=0 and pos2<=7:
        pos1-=1
        pos2+=1
        if (board[pos1][pos2]!='.' and (board[pos1][pos2]=='b' or board[pos1][pos2]=='q')):
                check=(k,board[pos1][pos2],pos1,pos2)
                break
    pos1=king_pos[k][0]
    pos2=king_pos[k][1] 
    
    if check!= None:
        return check
    
    while pos1<=7 and pos2<=7:
        pos1+=1
        pos2+=1
        if (board[pos1][pos2]!='.' and (board[pos1][pos2]=='b' or board[pos1][pos2]=='q')):
                check=(k,board[pos1][pos2],pos1,pos2)
                break
    pos1=king_pos[k][0]
    pos2=king_pos[k][1]  
    
    if check!= None:
        return check
    
    while pos1>=0 and pos2<=7:
        pos1-=1
        pos2+=1
        if (board[pos1][pos2]!='.' and (board[pos1][pos2]=='b' or board[pos1][pos2]=='q')):
                check=(k,board[pos1][pos2],pos1,pos2)
                break
            
    pos1=king_pos[k][0]
    pos2=king_pos[k][1]      
    
    return check
                    
if __name__ == '__main__':
    pass