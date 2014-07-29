
def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    kings = {}
    for i in range(0,7):
        for j in range(0,7):
            if (board[i][j]=='k'):
                kings['k']=(i,j)
            if (board[i][j]=='K'):
                kings['K']=(i,j)
        

    ''' Your code comes here '''
    print kings
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
    a=(king_pos[0])+1
    b=(king_pos[0])-1
    c=(king_pos[1])+1
    d=(king_pos[1])-1
    if (k=='k'):
        for i in c,d: 
            if (a<=7 and ((c<=7) or (d<=7))):
                if (board[a][i]=='P'):
                    return(k,'P',a,i)
                    break
    
    if (k=='K'):
        for i in c,d: 
            if (b<=7 and ((c<=7) or (d<=7))):
                if (board[a][i]=='p'):
                    return(k,'p',b,i)
                    break
                
    
    ''' You code comes here '''
        
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
    a=(king_pos[0])+1
    b=(king_pos[0])-1
    c=(king_pos[0])+2
    d=(king_pos[0])-2
    e=(king_pos[1])+1
    f=(king_pos[1])-1
    g=(king_pos[1])+2
    h=(king_pos[1])-2
    if (k=='k'):
        for i in g,h: 
            if (0<=a<=7 and ((0<=g<=7) or (0<=h<=7))):
                if (board[a][i]=='N'):
                    return(k,'N',a,i)
                    break
            if (0<=b<=7 and ((0<=g<=7) or (0<=h<=7))):
                if (board[b][i]=='N'):
                    return(k,'N',b,i)
                    break
        for i in e,f: 
            if (0<=c<=7 and ((0<=e<=7) or (0<=f<=7))):
                if (board[c][i]=='N'):
                    return(k,'N',a,i)
                    break
            if (0<=d<=7 and ((0<=e<=7) or (0<=f<=7))):
                if (board[d][i]=='N'):
                    return(k,'N',b,i)
                    break
        
    if (k=='K'):
        for i in g,h: 
            if (0<=a<=7 and ((0<=g<=7) or (0<=h<=7))):
                if (board[a][i]=='n'):
                    return(k,'n',a,i)
                    break
            if (0<=b<=7 and ((0<=g<=7) or (0<=h<=7))):
                if (board[b][i]=='n'):
                    return(k,'n',b,i)
                    break   
        for i in e,f: 
            if (0<=c<=7 and ((0<=e<=7) or (0<=f<=7))):
                if (board[c][i]=='n'):
                    return(k,'n',a,i)
                    break
            if (0<=d<=7 and ((0<=e<=7) or (0<=f<=7))):
                if (board[d][i]=='n'):
                    return(k,'n',b,i)
                    break    
    
    
    ''' You code comes here '''
        
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
    fkings=find_kings
    a=fkings['k']
    b=fkings['K']
    c=a[0]
    d=a[1]
    e=b[0]
    f=b[1]
    for i in range (c-1,c+2):
        if (0<=i<=7 and ((0<=d+1 <=7) or (0<=d-1<=7))):
            if (board[i][d+1]=='R' or 'Q'):
                return ('k',board[i][d+1],i,d+1)
                break
            elif (board[i][d-1]=='R' or 'Q'):
                return ('k',board[i][d-1],i,d-1)
                break
    for i in range (e-1,e+2):        
        if (0<=i<=7 and ((0<=f+1<=7) or(0<=f-1)<=7)):
            if (board[i][f+1]=='r' or 'q'):
                return ('K',board[i][f+1],i,f+1)
                break
            elif (board[i][f-1]=='r' or 'q'):
                return ('K',board[i][f-1],i,f-1)
                break
            
            
    for i in (c-1,c+1):
        if (0<=i<=7 and ((0<=d+1<=7) or(0<=d-1)<=7)):
            if (board[i][d+1]=='B' or 'Q'):
                return ('k',board[i][d+1],i,d+1)
                break
            elif (board[i][d-1]=='B' or 'Q'):
                return ('k',board[i][d-1],i,d-1)
                break
    
    for i in (e-1,e+1):        
        if (0<=i<=7 and ((0<=f+1<=7) or(0<=f-1)<=7)):
            if (board[i][f+1]=='b' or 'q'):
                return ('K',board[i][f+1],i,f+1)
                break
            elif (board[i][f-1]=='b' or 'q'):
                return ('K',board[i][f-1],i,f-1)    
                break
        
    return check
                    
if __name__ == '__main__':
    pass
