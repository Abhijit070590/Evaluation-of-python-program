
def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    kings = {}
    ''' Your code comes here '''       
    for x in board:
        for y in x:
            if(y=='k'):
                kings[y]+='k'
                king_position=()
                king_position+=(x,y)
                kings.append(king_position)
            if(y=='K'):
                kings[y]+='K'
                king_position=()
                king_position+=(x,y)
                kings.append(king_position)           
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
    for x in board:
        for y in x:
            if(y=='k'):
                if((x+1,y-1)=='P'):
                    print "(k,P,%d,%d)"%(x+1,y-1)
                elif((x+1,y+1)=='P'):
                    print "(k,P,%d,%d)"%(x+1,y+1)
                else:
                    print "None"
            elif(y=='K'):
                if((x-1,y-1)=='p'):
                    print "(K,p,%d,%d)"%(x-1,y-1)
                elif((x-1,y+1)=='p'):
                    print "(K,p,%d,%d)"%(x-1,y+1)
                else:
                    print "None"
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
    for x in board:
        for y in x:
            if(y=='k'):
                if((x+1,y-2)=='N'):
                    print "(k,N,%d,%d)"%(x+1,y-2)
                elif((x+1,y+2)=='N'):
                    print "(k,N,%d,%d)"%(x+1,y+2)
                elif((x-1,y-2)=='N'):    
                    print "(k,N,%d,%d)"%(x-1,y-2)
                elif((x-1,y+2)=='N'):    
                    print "(k,N,%d,%d)"%(x-1,y+2)
                elif((x-2,y-1)=='N'):    
                    print "(k,N,%d,%d)"%(x-2,y-1)    
                elif((x-2,y+1)=='N'):    
                    print "(k,N,%d,%d)"%(x-2,y+1)
                elif((x+2,y-1)=='N'):    
                    print "(k,N,%d,%d)"%(x+2,y-1)
                elif((x+2,y+1)=='N'):    
                    print "(k,N,%d,%d)"%(x+2,y+1)
                else:
                    print "None"
            elif(y=='K'):
                if((x-1,y-2)=='n'):
                    print "(K,n,%d,%d)"%(x-1,y-2)
                elif((x-1,y+2)=='n'):
                    print "(K,n,%d,%d)"%(x-1,y+2)
                elif((x+1,y-2)=='n'):    
                    print "(K,n,%d,%d)"%(x+1,y-2)
                elif((x+1,y+2)=='n'):    
                    print "(K,n,%d,%d)"%(x+1,y+2)
                elif((x-2,y-1)=='n'):    
                    print "(K,n,%d,%d)"%(x-2,y-1)
                elif((x-2,y+1)=='n'):    
                    print "(K,n,%d,%d)"%(x-2,y+1)
                elif((x+2,y-1)=='n'):    
                    print "(K,n,%d,%d)"%(x+2,y-1)
                elif((x+2,y+1)=='n'):    
                    print "(K,n,%d,%d)"%(x+2,y+1)
                else:
                    print "None"   
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
    check_pawn_attack()
    check_knight_attack()
    kings,x,y,k,K=find_kings
    kings[k]=(x,y)
    if((x-1,y)!='.' and (x-1,y)=='R'):
        print "(k,R,%d,%d)"%(x-1,y)
    elif((x+1,y)!='.'and(x+1,y)=='R'):
        print "(k,R,%d,%d)"%(x+1,y)
    elif((x,y-1)!='.'and(x,y-1)=='R'):
        print "(k,R,%d,%d)"%(x,y-1)
    elif((x,y+1)!='.'and(x,y+1)=='R'):
        print "(k,R,%d,%d)"%(x,y+1)
    
    
    if((x-1,y)!='.' and (x-1,y)=='Q'):
        print "(k,Q,%d,%d)"%(x-1,y)
    elif((x+1,y)!='.'and(x+1,y)=='Q'):
        print "(k,Q,%d,%d)"%(x+1,y)
    elif((x,y-1)!='.'and(x,y-1)=='Q'):
        print "(k,Q,%d,%d)"%(x,y-1)
    elif((x,y+1)!='.'and(x,y+1)=='Q'):
        print "(k,Q,%d,%d)"%(x,y+1)
    else:
        print "None"
    kings[K]=(x,y)
    if((x-1,y)!='.' and (x-1,y)=='r'):
        print "(K,r,%d,%d)"%(x-1,y)
    elif((x+1,y)!='.'and(x+1,y)=='r'):
        print "(K,r,%d,%d)"%(x+1,y)
    elif((x,y-1)!='.'and(x,y-1)=='r'):
        print "(K,r,%d,%d)"%(x,y-1)
    elif((x,y+1)!='.'and(x,y+1)=='r'):
        print "(K,r,%d,%d)"%(x,y+1)
    
    if((x-1,y)!='.' and (x-1,y)=='q'):
        print "(K,q,%d,%d)"%(x-1,y)
    elif((x+1,y)!='.'and(x+1,y)=='q'):
        print "(K,q,%d,%d)"%(x+1,y)
    elif((x,y-1)!='.'and(x,y-1)=='q'):
        print "(K,q,%d,%d)"%(x,y-1)
    elif((x,y+1)!='.'and(x,y+1)=='q'):
        print "(K,q,%d,%d)"%(x,y+1)
        
    else:
        print "None"
        
    kings[k]=(x,y)
    if((x-1,y-1)!='.' and (x-1,y-1)=='B'):
        print "(k,B,%d,%d)"%(x-1,y-1)
    elif((x+1,y+1)!='.'and(x+1,y+1)=='B'):
        print "(k,B,%d,%d)"%(x+1,y+1)
    elif((x+1,y-1)!='.'and(x+1,y-1)=='B'):
        print "(k,B,%d,%d)"%(x+1,y-1)
    elif((x-1,y+1)!='.'and(x,y+1)=='R'):
        print "(k,B,%d,%d)"%(x-1,y+1)
    
    if((x-1,y-1)!='.' and (x-1,y-1)=='Q'):
        print "(k,Q,%d,%d)"%(x-1,y-1)
    elif((x+1,y-1)!='.'and(x+1,y-1)=='Q'):
        print "(k,Q,%d,%d)"%(x+1,y-1)
    elif((x+1,y+1)!='.'and(x,y-1)=='Q'):
        print "(k,Q,%d,%d)"%(x+1,y+1)
    elif((x-1,y+1)!='.'and(x-1,y+1)=='Q'):
        print "(k,Q,%d,%d)"%(x-1,y+1)
    kings[K]=(x,y)
    if((x-1,y-1)!='.' and (x-1,y-1)=='b'):
        print "(K,b,%d,%d)"%(x-1,y-1)
    elif((x+1,y+1)!='.'and(x+1,y+1)=='b'):
        print "(K,b,%d,%d)"%(x+1,y+1)
    elif((x+1,y-1)!='.'and(x+1,y-1)=='b'):
        print "(K,b,%d,%d)"%(x+1,y-1)
    elif((x-1,y+1)!='.'and(x-1,y+1)=='b'):
        print "(K,b,%d,%d)"%(x-1,y+1)
    
    if((x-1,y-1)!='.' and (x-1,y-1)=='q'):
        print "(K,q,%d,%d)"%(x-1,y-1)
    elif((x+1,y+1)!='.'and(x+1,y+1)=='q'):
        print "(K,q,%d,%d)"%(x+1,y+1)
    elif((x+1,y-1)!='.'and(x+1,y-1)=='q'):
        print "(K,q,%d,%d)"%(x+1,y-1)
    elif((x-1,y+1)!='.'and(x-1,y+1)=='q'):
        print "(K,q,%d,%d)"%(x-1,y+1)
    else:
        print "None"
    return check
                    
if __name__ == '__main__':
    pass
