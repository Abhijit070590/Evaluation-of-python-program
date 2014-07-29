
def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    kings = {}
    for i in p:
        for j in i:
            if(j=='k'):
                r=1
                while(r<=7):
                    x=p[r].index('k')
                w=p.index('k')
            elif(j=='K'):
                q=1
                while(q<=7):
                    y=p[q].index('K')
                z=p.index('K')
    t1=(w,x)
    t2=(z,y)
    print 'position of black king is'
    print t1
    print 'position of white king is'
    print t2    
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
        
    return check
                    
if __name__ == '__main__':
    pass
l0=raw_input("enter row 0")
l1=raw_input("enter row 1")
l2=raw_input("enter row 2")
l3=raw_input("enter row 3")
l4=raw_input("enter row 4")
l5=raw_input("enter row 5")
l6=raw_input("enter row 6")
l7=raw_input("enter row 7")
p=[]
a=list(l0)
b=list(l1)
c=list(l2)
d=list(l3)
e=list(l4)
f=list(l5)
g=list(l6)
h=list(l7)
p.append(a)
p.append(b)
p.append(c)
p.append(d)
p.append(e)
p.append(f)
p.append(g)
p.append(h)
print p
find_kings(p)
