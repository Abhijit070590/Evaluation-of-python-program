def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    x=0
    kings = {}
    while(x<8):
        y=0
        while(y<8):
            if(board[0][x][y]=='k'):
                kings['k']=(x,y)
            if(board[0][x][y]=='K'):
                kings['K']=(x,y)
            y=y+1
        x=x+1
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
    x=0
    while(x<8):
        y=0
        while(y<8):
            if(board[0][x][y]=='p'):
                pos_p=(x,y)
            if(board[0][x][y]=='P'):
                pos_P=(x,y)
            y=y+1
        x=x+1
    if(k=='k'):
        print 'We are considering Black king to check pawn attack'
        if(king_pos[0]+1==pos_P[0] and king_pos[1]+1==pos_P[1]):
            print 'check mate'
            return (k, 'P', pos_P[0], pos_P[1])
        elif(king_pos[0]+1==pos_P[0] and king_pos[1]-1==pos_P[1]):
            print 'check mate'
            return (k, 'P', pos_P[0], pos_P[1])
        elif(king_pos[0]-1==pos_P[0] and king_pos[1]+1==pos_P[1]):
            print 'check mate'
            return (k, 'P', pos_P[0], pos_P[1])
        elif(king_pos[0]-1==pos_P[0] and king_pos[1]-1==pos_P[1]):
            print 'check mate'
            return (k, 'P', pos_P[0], pos_P[1])

    elif(k=='K'):
        print 'We are considering White king to check pawn attack'
        if(king_pos[0]+1==pos_p[0] and king_pos[1]+1==pos_p[1]):
            print 'check mate'
            return (k, 'P', pos_p[0], pos_p[1])
        elif(king_pos[0]+1==pos_p[0] and king_pos[1]-1==pos_p[1]):
            print 'check mate'
            return (k, 'P', pos_p[0], pos_p[1])
        elif(king_pos[0]-1==pos_p[0] and king_pos[1]+1==pos_p[1]):
            print 'check mate'
            return (k, 'P', pos_p[0], pos_p[1])
        elif(king_pos[0]-1==pos_p[0] and king_pos[1]-1==pos_p[1]):
            print 'check mate'
            return (k, 'P', pos_p[0], pos_p[1])
    
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
    x=0
    while(x<8):
        y=0
        while(y<8):
            if(board[0][x][y]=='n'):
                pos_n=(x,y)
            if(board[0][x][y]=='N'):
                pos_N=(x,y)
            y=y+1
        x=x+1
    move_x=0
    move_y=0
    if(k=='k'):
        print 'We are considering Black king to check knight attack'
        
        while(move_x!=king_pos[0] or move_y!=king_pos[1]):
            move_x=pos_N[0] + 1
            move_y=pos_N[1] + 2
            if(move_x==king_pos[0] and move_y==king_pos[1]):
                print 'check mate'
                return (k, 'N', pos_N[0], pos_N[1])
            move_x=pos_N[0] + 1
            move_y=pos_N[1] - 2
            if(move_x==king_pos[0] and move_y==king_pos[1]):
                print 'check mate'
                return (k, 'N', pos_N[0], pos_N[1])
            move_x=pos_N[0] - 1
            move_y=pos_N[1] + 2
            if(move_x==king_pos[0] and move_y==king_pos[1]):
                print 'check mate'
                return (k, 'N', pos_N[0], pos_N[1])
            move_x=pos_N[0] - 1
            move_y=pos_N[1] - 2
            if(move_x==king_pos[0] and move_y==king_pos[1]):
                print 'check mate'
                return (k, 'N', pos_N[0], pos_N[1])
            move_x=pos_N[0] + 2
            move_y=pos_N[1] + 1
            if(move_x==king_pos[0] and move_y==king_pos[1]):
                print 'check mate'
                return (k, 'N', pos_N[0], pos_N[1])
            move_x=pos_N[0] + 2
            move_y=pos_N[1] - 1
            if(move_x==king_pos[0] and move_y==king_pos[1]):
                print 'check mate'
                return (k, 'N', pos_N[0], pos_N[1])
            move_x=pos_N[0] - 2
            move_y=pos_N[1] + 1
            if(move_x==king_pos[0] and move_y==king_pos[1]):
                print 'check mate'
                return (k, 'N', pos_N[0], pos_N[1])
            move_x=pos_N[0] - 2
            move_y=pos_N[1] + 1
            if(move_x==king_pos[0] and move_y==king_pos[1]):
                print 'check mate'
                return (k, 'N', pos_N[0], pos_N[1])
            break
    
    
    else:
        print 'We are considering White king to check knight attack'
        while(move_x!=king_pos[0] or move_y!=king_pos[1]):
            move_x=pos_n[0] + 1
            move_y=pos_n[1] + 2
            if(move_x==king_pos[0] and move_y==king_pos[1]):
                print 'check mate'
                return (k, 'N', pos_n[0], pos_n[1])
            move_x=pos_n[0] + 1
            move_y=pos_n[1] - 2
            if(move_x==king_pos[0] and move_y==king_pos[1]):
                print 'check mate'
                return (k, 'N', pos_n[0], pos_n[1])
            move_x=pos_n[0] - 1
            move_y=pos_n[1] + 2
            if(move_x==king_pos[0] and move_y==king_pos[1]):
                print 'check mate'
                return (k, 'N', pos_n[0], pos_n[1])
            move_x=pos_n[0] - 1
            move_y=pos_n[1] - 2
            if(move_x==king_pos[0] and move_y==king_pos[1]):
                print 'check mate'
                return (k, 'N', pos_n[0], pos_n[1])
            move_x=pos_n[0] + 2
            move_y=pos_n[1] + 1
            if(move_x==king_pos[0] and move_y==king_pos[1]):
                print 'check mate'
                return (k, 'N', pos_n[0], pos_n[1])
            move_x=pos_n[0] + 2
            move_y=pos_n[1] - 1
            if(move_x==king_pos[0] and move_y==king_pos[1]):
                print 'check mate'
                return (k, 'N', pos_n[0], pos_n[1])
            move_x=pos_n[0] - 2
            move_y=pos_n[1] + 1
            if(move_x==king_pos[0] and move_y==king_pos[1]):
                print 'check mate'
                return (k, 'N', pos_n[0], pos_n[1])
            move_x=pos_n[0] - 2
            move_y=pos_n[1] + 1
            if(move_x==king_pos[0] and move_y==king_pos[1]):
                print 'check mate'
                return (k, 'N', pos_n[0], pos_n[1])
            break
        
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
    
    knight=check_knight_attack(board, king, position)
    print knight
    pawn=check_pawn_attack(board, king, position)
    print pawn
    king_detail=find_kings(board)
    pos_Q=()
    pos_R=()
    pos_B=()
    pos_q=()
    pos_r=()
    pos_b=()
    x=0
    while(x<8):
        y=0
        while(y<8):
            if(board[0][x][y]=='r'):
                pos_r=(x,y)
            if(board[0][x][y]=='R'):
                pos_R=(x,y)
            if(board[0][x][y]=='q'):
                pos_q=(x,y)
            if(board[0][x][y]=='Q'):
                pos_Q=(x,y)
            if(board[0][x][y]=='b'):
                pos_b=(x,y)
            if(board[0][x][y]=='B'):
                pos_B=(x,y)
            y=y+1
        x=x+1
    for k, king_pos in king_detail.items():
        if(k=='k'):
            print 'We are considering Black king to check rook or queen attack'
            if(king_pos[0]==pos_Q[0] and king_pos[1]+1==pos_Q[1]):
                print 'check mate'
                return (k, 'Q', pos_Q[0], pos_Q[1])
            elif(king_pos[0]==pos_R[0] and king_pos[1]+1==pos_R[1]):
                print 'check mate'
                return (k, 'R', pos_R[0], pos_R[1])
            elif(king_pos[0]==pos_Q[0] and king_pos[1]-1==pos_Q[1]):
                print 'check mate'
                return (k, 'Q', pos_Q[0], pos_Q[1])
            elif(king_pos[0]==pos_R[0] and king_pos[1]-1==pos_R[1]):
                print 'check mate'
                return (k, 'R', pos_R[0], pos_R[1])
            elif(king_pos[0]+1==pos_Q[0] and king_pos[1]==pos_Q[1]):
                print 'check mate'
                return (k, 'Q', pos_Q[0], pos_Q[1])
            elif(king_pos[0]+1==pos_R[0] and king_pos[1]==pos_R[1]):
                print 'check mate'
                return (k, 'R', pos_R[0], pos_R[1])
            elif(king_pos[0]-1==pos_Q[0] and king_pos[1]==pos_Q[1]):
                print 'check mate'
                return (k, 'Q', pos_Q[0], pos_Q[1])
            elif(king_pos[0]-1==pos_R[0] and king_pos[1]==pos_R[1]):
                print 'check mate'
                return (k, 'R', pos_R[0], pos_R[1])
            elif(king_pos[0]+1==pos_Q[0] and king_pos[1]+1==pos_Q[1]):
                print 'check mate'
                return (k, 'Q', pos_Q[0], pos_Q[1])
            elif(king_pos[0]+1==pos_B[0] and king_pos[1]+1==pos_B[1]):
                print 'check mate'
                return (k, 'B', pos_B[0], pos_B[1])
            elif(king_pos[0]+1==pos_Q[0] and king_pos[1]-1==pos_Q[1]):
                print 'check mate'
                return (k, 'Q', pos_Q[0], pos_Q[1])
            elif(king_pos[0]+1==pos_B[0] and king_pos[1]-1==pos_B[1]):
                print 'check mate'
                return (k, 'B', pos_B[0], pos_B[1])
            elif(king_pos[0]-1==pos_Q[0] and king_pos[1]-1==pos_Q[1]):
                print 'check mate'
                return (k, 'Q', pos_Q[0], pos_Q[1])
            elif(king_pos[0]-1==pos_B[0] and king_pos[1]-1==pos_B[1]):
                print 'check mate'
                return (k, 'B', pos_B[0], pos_B[1])
            elif(king_pos[0]-1==pos_Q[0] and king_pos[1]+1==pos_Q[1]):
                print 'check mate'
                return (k, 'Q', pos_Q[0], pos_Q[1])
            elif(king_pos[0]-1==pos_B[0] and king_pos[1]+1==pos_B[1]):
                print 'check mate'
                return (k, 'B', pos_B[0], pos_B[1])
        elif(k=='K'):
            print 'We are considering White king to check rook or queen attack'
            if(king_pos[0]==pos_q[0] and king_pos[1]+1==pos_q[1]):
                print 'check mate'
                return (k, 'q', pos_q[0], pos_q[1])
            elif(king_pos[0]==pos_r[0] and king_pos[1]+1==pos_r[1]):
                print 'check mate'
                return (k, 'r', pos_r[0], pos_r[1])
            elif(king_pos[0]==pos_q[0] and king_pos[1]-1==pos_q[1]):
                print 'check mate'
                return (k, 'q', pos_q[0], pos_q[1])
            elif(king_pos[0]==pos_r[0] and king_pos[1]-1==pos_r[1]):
                print 'check mate'
                return (k, 'r', pos_r[0], pos_r[1])
            elif(king_pos[0]+1==pos_q[0] and king_pos[1]==pos_q[1]):
                print 'check mate'
                return (k, 'q', pos_q[0], pos_q[1])
            elif(king_pos[0]+1==pos_r[0] and king_pos[1]==pos_r[1]):
                print 'check mate'
                return (k, 'r', pos_r[0], pos_r[1])
            elif(king_pos[0]-1==pos_q[0] and king_pos[1]==pos_q[1]):
                print 'check mate'
                return (k, 'q', pos_q[0], pos_q[1])
            elif(king_pos[0]-1==pos_r[0] and king_pos[1]==pos_r[1]):
                print 'check mate'
                return (k, 'r', pos_r[0], pos_r[1])
            elif(king_pos[0]+1==pos_q[0] and king_pos[1]+1==pos_q[1]):
                print 'check mate'
                return (k, 'q', pos_q[0], pos_q[1])
            elif(king_pos[0]+1==pos_b[0] and king_pos[1]+1==pos_b[1]):
                print 'check mate'
                return (k, 'b', pos_B[0], pos_B[1])
            elif(king_pos[0]+1==pos_q[0] and king_pos[1]-1==pos_q[1]):
                print 'check mate'
                return (k, 'q', pos_q[0], pos_q[1])
            elif(king_pos[0]+1==pos_b[0] and king_pos[1]-1==pos_b[1]):
                print 'check mate'
                return (k, 'b', pos_B[0], pos_B[1])
            elif(king_pos[0]-1==pos_q[0] and king_pos[1]-1==pos_q[1]):
                print 'check mate'
                return (k, 'q', pos_q[0], pos_q[1])
            elif(king_pos[0]-1==pos_b[0] and king_pos[1]-1==pos_b[1]):
                print 'check mate'
                return (k, 'b', pos_b[0], pos_b[1])
            elif(king_pos[0]-1==pos_q[0] and king_pos[1]+1==pos_q[1]):
                print 'check mate'
                return (k, 'q', pos_q[0], pos_q[1])
            elif(king_pos[0]-1==pos_b[0] and king_pos[1]+1==pos_b[1]):
                print 'check mate'
                return (k, 'b', pos_b[0], pos_b[1])
    
    return check
                    

detail={}
'''for checking purpose I have included board'''
board=((           [['.','.','.','r','k','b','.','r'],
                    ['.','.','N','.','.','p','p','.'],
                    ['p','.','P','p','.','.','.','p'],
                    ['.','p','n','.','.','P','.','.'],
                    ['.','.','.','.','.','.','.','.'],
                    ['.','.','.','.','P','.','.','.'],
                    ['P','.','.','.','.','.','P','P'],
                    ['R','.','.','.','.','R','K','.']], (0,4), (7,6), ('k','N', 1, 2)))
detail=find_kings(board)
print 'Contents of Dictionary: '
for king, position in detail.items():
    print 'king %s position= %s' % (king, position)
    check_check(board)
