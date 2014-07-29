
def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
def king_pos(row,col):
    kings={}
    l=[['r','n','b','q','k','b','n','r'],
     ['p','p','p','p','p','p','p','p'],
         ['.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.'],
         ['P','P','P','P','P','P','P','P'],
         ['R','N','B','Q','K','B','N','R']]
    def attacker(Pawn,Bishop,Knight,Queen,Rook):
        def check_pawn_attack(board, k, king_pos):
            return kings(king_pos)
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
    
    """You code comes here"""
    attacker_x={-1,1}
    attacker_y={-1,+1}
if(p(-1,-1)=king_pos(K)or p(-1,1)=king_pos(K))
    print (p,K,attacker_x,attacker_y)
if P(1,+/-1)=king_pos(k)
    print (P,k,attacker_x,attacker_y)
def pos_attacker(attacker_x,attacker_y):
else
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

if(attacker={+/-1,+/-2} and attacker_y={+/-2,+/-1})
 attacker_y={+/-2,+/-1}
    if (n(+/-1,+/-2)=King_pos(K) or n(+/- 2,+/-1)=king_pos(K))
        print (n,K,attacker_x,attacker_y)
        
    if (N(+/-1,+/-2)=King_pos(k) or N(+/- 2,+/-1)=king_pos(K))
        print (N,k,attacker_x,attacker_y)
     
else
     return none

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
    if(check_knight_attack=1)
     if(pos_king(k)-pos_attacker(Q) or pos_king(k)-pos_attacker(R)=(0,1)or(0,-1)or(1,0)or(-1,0))
        return (k,attacker,attacker_x,attacker_y)
        if(pos_king(K)-pos_attacker(q)or pos_king(K)-pos_attacker(r)=(0,1)or(0,-1)or(1,0)or(-1,0))
         return (k,attacker,attacker_x,attacker_y)
     else
        return check
    elseif(check_pawn_attack=1)
    if(pos_king(k)-pos_attacker(Q) or pos_king(k)-pos_attacker(B)=(0,1)or(0,-1)or(1,0)or(-1,0))
        return (k,attacker,attacker_x,attacker_y) 
     if(pos_king(K)-pos_attacker(q) or pos_king(K)-pos_attacker(b)=(0,1)or(0,-1)or(1,0)or(-1,0))
        return (k,attacker,attacker_x,attacker_y)   
     else
        return check
     
           
   
                    
if __name__ == '__main__':
    pass