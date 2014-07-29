king_pos=()
def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    kings = {}
    for a in board:
        for b in a:
            if b=='k' or b=='K':
                king_pos.append(king_pos[0],king_pos[1])
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
    a=king_pos[0],b=king_pos[1]
    for x in board:
        for y in x:
            if y=='k':
                if (a+1,b)==('P'):
                    return ('k','P',a+1,b+1)
                elif (a,b+1)==('P'):
                    return ('k','P',a,b+1)
                elif (a-1,b)==('P'):
                    return ('k','P',a-1,b)
                elif (a,b-1)==('P'):
                    return ('k','P',a,b-1)
                else:        
                    return check
            elif y=='K':
                if (a+1,b)==('p'):
                    return ('K','p',a+1,b)
                elif (a-1,b)==('p'):
                    return ('K','p',a-1,b)
                elif (a,b+1)==('p'):
                    return ('K','p',a,b+1)
                elif (a,b-1)==('p'):
                    return ('K','p',a,b-1)
                else:        
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
    c=king_pos[0],d=king_pos[1]
    for x in board:
        for y in x:
            if y=='k':
                if (c+1,d)==('N'):
                    return ('k','N',c+1,d)
                elif (c,d+1)==('N'):
                    return ('k','N',c,d+1)
                elif (c-1,d)==('N'):
                    return ('k','N',c-1,d)
                elif (c,d-1)==('N'):
                    return ('k','N',c,d-1)
                else:
                    return check   
            elif y=='K':
                if (c+1,d)==('n'):
                    return ('k','n',c+1,d)
                elif (c,d+1)==(''):
                    return ('k','',c,d+1)
                elif (c-1,d)==(''):
                    return ('k','n',c-1,d)
                elif (c,d-1)==('n'):
                    return ('k','n',c,d-1)
                else:
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
    check_pawn_attack()
    check_knight_attack()
    e=king_pos[0],f=king_pos[1]
    for x in board:
        for y in x:
            if y=='k':
                if (e+1,f)==('Q'):
                    return ('k','Q',e+1,f)
                elif (e,f+1)==('Q'):
                    return ('k','Q',e,f+1)
                elif (e-1,f)==('Q'):
                    return ('k','Q',e-1,f)
                elif (e,f-1)==('Q'):
                    return ('k','Q',e,f-1)
                else:
                    return check   
            elif y=='K':
                if (e+1,f)==('q'):
                    return ('k','q',e+1,f)
                elif (e,f+1)==(''):
                    return ('k','q',e,f+1)
                elif (e-1,f)==('q'):
                    return ('k','q',e-1,f)
                elif (e,f-1)==('q'):
                    return ('k','q',e,f-1)
                else:
                    return check  
            if y=='k':
                if (e+1,f)==('B'):
                    return ('k','B',e+1,f)
                elif (e,f+1)==('B'):
                    return ('k','B',e,f+1)
                elif (e-1,f)==('B'):
                    return ('k','B',e-1,f)
                elif (e,f-1)==('B'):
                    return ('k','B',e,f-1)
                else:
                    return check   
            elif y=='K':
                if (e+1,f)==('b'):
                    return ('k','b',e+1,f)
                elif (e,f+1)==('b'):
                    return ('k','b',e,f+1)
                elif (e-1,f)==('b'):
                    return ('k','b',e-1,f)
                elif (e,f-1)==('b'):
                    return ('k','b',e,f-1)
                else:
                    return check  
         
                    
if __name__ == '__main__':
    pass
