
def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    kings = {}

    ''' Your code comes here '''
    position_k=[0]*2
    position_K=[0]*2
    countk=-1
    counti=-1
    
    for i in board:
        counti+=1
        for k in i:
            countk+=1
            if (k=='k'):
                kings['k']=(counti,countk)
            if(k=='K'):
                kings['K']=(counti,countk)
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
    i=king_pos[0]-1
    countj=-1
    if(k=='K'):
            for j in board[i]:
                countj+=1
                if(j=='p'):
                    check=('K','p',counti,countj)
            for j in i:
                if(j=='p'):
                    check=('K','p',counti,countj)
            else:
                check=('none')   
    
     
    if(k=='k'):
        i=king_pos[0]+1
        countj=-1
        for j in board[i]:
            countj+=1
            if(j=='P'):
                position_p=[i,j]
                check=('K','P',i,j)
        for j in i:
            if(j=='P'):
                position_p=[i,j]
                check=('K','P',i,j)
            else:
                check=('none')         
    
                          
                    
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
    i=king_pos[0]+1
    j=king_pos[1]
    if(k=='K'):
        for i in board:
            for j in i:
                if(j=='n'):
                    check=('K','n',i,j)
                elif(j=='n'):
                    check=('K','n',i,j)
                else:
                    check=('none')    
        i=king_pos[0]-1            
        for i in board:
            for j in i:
                if(j=='n'):
                    check=('K','n',i,j)
                elif(j=='n'):
                    check=('K','n',i,j) 
                else:
                    check=('none')   
        i=king_pos[0]+2                    
        for i in board:
            for j in i:
                if(j=='n'):
                    check=('K','n',i,j)
                elif(k+1=='n'):
                    check=('K','n',i,j) 
                else:
                    check=['none']      
        for i in board:
            for j in i:
                if(j=='n'):
                    check=('K','n',i-2,j)
                elif(j=='n'):
                    check=('K','n',i-2,j)    
                else:
                    check=('none')                             
                    
        
    if(k=='k'):
        for i in board:
            for j in i:
                if(j=='N'):
                    check=('k','N',i,j)
                elif(j=='N'):
                    check=('k','N',i,j)
                else:
                    check=('none')    
        i=king_pos[0]-1            
        for i in board:
            for j in i:
                if(j=='N'):
                    check=('k','N',i,j)
                elif(j=='N'):
                    check=('k','N',i,j) 
                else:
                    check=('none')   
        i=king_pos[0]+2                    
        for i in board:
            for j in i:
                if(j=='N'):
                    check=('k','N',i,j)
                elif(k+1=='N'):
                    check=('k','N',i,j) 
                else:
                    check=['none']      
        for i in board:
            for j in i:
                if(j=='N'):
                    check=('k','N',i-2,j)
                elif(j=='N'):
                    check=('k','N',i-2,j)    
                else:
                    check=('none')                
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
    for l in board:
        for m in i:
            if(m=='K'):
                pos_x=l
                pos_y=m
                break
    i=pos_x-1
   
    if(k=='K'):
        for i in board:
            for j in i:
                if(j=='p'):
                    position_p=[i,j]
                    check=('K','p',i,j)
            for j in i:
                if(j=='p'):
                    position_p=[i-1,j]
                    check=('K','p',i-1,j)
            else:
                check=('none')      
    
    if(k=='k'):
        i=pos_x+1
        for i in board:
            for j in i:
                if(j=='P'):
                    position_p=[i,j]
                    check=('K','P',i,j)
            for j in i:
                if(j=='P'):
                    position_p=[i+1,j]
                    check=('K','P',i+1,j)
            else:
                check=('none')      
                
    if (k=='K'):
        for i in board:
            for j in i:
                if(j=='n'):
                    check=('K','n',i,j)
                elif(j=='n'):
                    check=('K','n',i,j)
                else:
                    check=('none')    
        i=pos_x-1            
        for i in board:
            for j in i:
                if(j=='n'):
                    check=('K','n',i,j)
                elif(j=='n'):
                    check=('K','n',i,j) 
                else:
                    check=('none')      
        i=pos_x+2                 
        for i in board:
            for j in i:
                if(j=='n'):
                    check=('K','n',i,j)
                elif(j=='n'):
                    check=('K','n',i,j) 
                else:
                    check=('none')   
        i=pos_x-2               
        for i in board:
            for j in i:
                if(j=='n'):
                    check=('K','n',i,j)
                elif(k+1=='n'):
                    check=('K','n',i,j)    
                else:
                    check=('none')                            
        return check                                             
    if __name__ == '__main__':
       pass