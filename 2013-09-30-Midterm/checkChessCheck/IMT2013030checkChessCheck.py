
def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    kings = {}
    kx=0
    ky=0
    Kx=0
    Ky=0
    for x in board:
        for y in x:
            if y=='k':
                kx=board.index(x)
                ky=x.index(y)
            if y=='K':
                Kx=board.index(x)
                Ky=x.index(y)
    kings["k"]=(kx,ky)
    kings["K"]=(Kx,Ky)
 

    ''' Your code comes here '''
    
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
    #check inner area
    if(king_pos[0] not in [0,7] or king_pos not in [0,1]):
        if (k=='k'):
            if(board[king_pos[0]+1][king_pos[1]-1]=='P'):
                check=(k,"P",king_pos[0]+1,king_pos[1]-1)
            if(board[king_pos[0]+1][king_pos[1]+1]=='P'):
                check=(k,"P",king_pos[0]+1,king_pos[1]+1)
        if (k=='K'):
            if(board[king_pos[0]-1][king_pos[1]-1]=='P'):
                check=(k,"P",king_pos[0]-1,king_pos[1]-1)
            if(board[king_pos[0]-1][king_pos[1]+1]=='P'):
                check=(k,"P",king_pos[0]-1,king_pos[1]+1)
                
    #check top and bottom
    if (king_pos[0]==0 and king_pos[1]!=0 and k=='k'):
        if(board[king_pos[0]+1][king_pos[1]-1]=='P'):
                check=(k,"P",king_pos[0]+1,king_pos[1]-1)
        if(board[king_pos[0]+1][king_pos[1]+1]=='P'):
                check=(k,"P",king_pos[0]+1,king_pos[1]+1)
    if (king_pos[0]==0 and king_pos[1]==0 and k=='k'):
        if(board[1][1]=='P'):
                check=(k,"P",1,1)
    if (king_pos[0]==7 and king_pos[1]!=0 and k=='K'):
        if(board[king_pos[0]-1][king_pos[1]-1]=='p'):
                check=(k,"p",king_pos[0]-1,king_pos[1]-1)
        if(board[king_pos[0]-1][king_pos[1]+1]=='p'):
                check=(k,"p",king_pos[0]-1,king_pos[1]+1)
    if (king_pos[0]==7 and king_pos[1]==7 and k=='K'):
        if(board[6][6]=='p'):
                check=(k,"p",6,6) 
    
    #check sides
    if(king_pos[1]==0):
        if (k=='k'):
            if(board[king_pos[0]+1][1]=='P'):
                check=(k,"P",king_pos[0]+1,1)
        if (k=='K'):
            if(board[king_pos[0]-1][1]=='p'):
                check=(k,"p",king_pos[0]-1,1)
    if(king_pos[1]==7):
        if (k=='k'):
            if(board[king_pos[0]+1][6]=='P'):
                check=(k,"P",king_pos[0]+1,6)
        if (k=='K'):
            if(board[king_pos[0]-1][6]=='p'):
                check=(k,"p",king_pos[0]-1,6)
            
        
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
    nx=[]
    ny=[]
    Nx=[]
    Ny=[]
    for x in board:
        for y in x:
            if y=='n':
                nx.append(board.index(x))
                ny.append(x.index(y))
            if y=='N':
                Nx.append(board.index(x))
                Ny.append(x.index(y))
    if(k=='k'):
        if(king_pos in [(Nx[0]-2,Ny[0]+1),(Nx[0]-1,Ny[0]+2),(Nx[0]+1,Ny[0]+2),(Nx[0]+2,Ny[0]+1),(Nx[0]-2,Ny[0]-1),\
                        (Nx[0]-1,Ny[0]-2),(Nx[0]+1,Ny[0]-2),(Nx[0]+2,Ny[0]-1)]):
            check=(k,'N',Nx[0],Ny[0])
        if(king_pos in [(Nx[1]-2,Ny[1]+1),(Nx[1]-1,Ny[1]+2),(Nx[1]+1,Ny[1]+2),(Nx[1]+2,Ny[1]+1),(Nx[1]-2,Ny[1]-1),\
                        (Nx[1]-1,Ny[1]-2),(Nx[1]+1,Ny[1]-2),(Nx[1]+2,Ny[1]-1)]):
            check=(k,'N',Nx[1],Ny[1])   
    if(k=='K'):
        if(king_pos in [(nx[0]-2,ny[0]+1),(nx[0]-1,ny[0]+2),(nx[0]+1,ny[0]+2),(nx[0]+2,ny[0]+1),(nx[0]-2,ny[0]-1),\
                        (nx[0]-1,ny[0]-2),(nx[0]+1,ny[0]-2),(nx[0]+2,ny[0]-1)]):
            check=(k,'n',nx[0],ny[0])     
        if(king_pos in [(nx[1]-2,ny[1]+1),(nx[1]-1,ny[1]+2),(nx[1]+1,ny[1]+2),(nx[1]+2,ny[1]+1),(nx[1]-2,ny[1]-1),\
                        (nx[1]-1,ny[1]-2),(nx[1]+1,ny[1]-2),(nx[1]+2,ny[1]-1)]):
            check=(k,'n',nx[1],ny[1]) 
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
    
    pos=find_kings(board)
    pos_k=pos["k"]
    pos_K=pos["K"]
    check=check_pawn_attack(board,'k', pos_k)
    check=check_pawn_attack(board,'K', pos_K)
    check=check_knight_attack(board,'k', pos_k)
    check=check_knight_attack(board,'K', pos_K)
    rqx=[]
    rqy=[]
    RQx=[]
    RQy=[]
    if check!=None:
        for x in board:
            for y in x:
                if (y=='r' or y=='q'):
                    rqx.append(board.index(x))
                    rqy.append(x.index(y))
                if (y=='R' or y=='Q'):
                    RQx.append(board.index(x))
                    RQy.append(x.index(y))
        for i in range(len(board)):
            for j in rqx:
                if ((i!=j) and (pos_K[0]==i+1 or pos_K[0]==i-1)):
                    if(pos_K[0]==i+1):
                        pos_K[0]=i
                        break
                    if(pos_K[0]==i-1):
                        pos_K[0]=i
                        break
        
                                    
            
            
            
    
    
    ''' You code comes here '''
        
    return check
                    
if __name__ == '__main__':
    pass