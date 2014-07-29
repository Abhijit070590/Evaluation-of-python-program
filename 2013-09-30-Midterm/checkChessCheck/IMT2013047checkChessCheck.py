
def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                    if(board[i][j]=='k'):
                        value1=(i,j)
                        
                    elif(board[i][j]=='K'):
                        value2=(i,j)
    
    kings={'k':value1,'K':value2}
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
    def cmpT(tuple1,tuple2):
            if tuple1==tuple2:
                    return "True"
            else:
                    return "False"
                    
    pawns={}
    final={}
    for i in range(1,len(board)-1):
            for j in range(0,len(board[i])):
                    if(board[i][j]=='p'):
                            pawns['p']=(i,j)
                    elif(board[i][j]=='P'):
                            pawns['P']=(i,j)
                            
    if(k=='K'):
            for key,value in pawns.items():
                if(key=='p'):
                    lst1=list(value)
                    lst2=lst1[:]
                    lst1[0]=lst1[0]+1
                    lst1[1]=lst1[1]+1
                    lst2[0]=lst2[0]+1
                    lst2[1]=lst2[2]-1
                    value1=tuple(lst1)
                    value2=tuple(lst2)
                    if(cmpT(value1,king_pos)=="True"):
                            return (k,'p',value[0],value[1])
                            
                    elif(cmpT(value2,king_pos)=="True"):
                            return (k,'p',value[0],value[1])
    elif(k=='k'):
            for key,value in pawns.items():
                    if(key=='P'):
                        lst1=list(value)
                        lst2=lst1[:]
                        lst1[0]=lst1[0]-1
                        lst1[1]=lst1[1]+1
                        lst2[0]=lst2[0]-1
                        lst2[1]=lst2[1]-1
                        value1=tuple(lst1)
                        value2=tuple(lst2)
                        if(cmpT(value1,king_pos)=="True"):
                                final=(k,'P',value[0],value[1])
                        
                        elif(cmpT(value2,king_pos)=="True"):
                                final=(k,'P',value[0],value[1])
                                
    return final
                              
                         

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


board = [['.','.','.','.','.','.','.','.'],
         ['.','.','.','k','.','.','.','.'],
         ['.','p','n','.','p','.','.','.'],
         ['.','p','.','.','P','p','.','.'],
         ['.','.','.','K','.','P','.','.'],
         ['.','R','.','.','.','.','.','R'],
         ['P','P','.','.','.','.','.','.'],
         ['.','.','B','.','.','.','.','.']]
