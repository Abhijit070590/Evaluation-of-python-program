'''
Created on Sep 30, 2013

@author: imt2013006
'''
def legal_pos (i,j):
        if (i<8 and j<8):
            return 1
        else:
            return 0

def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    kings = {}
    i=0
    j=0
    while(i<len(board)):
        while(j<8):
            if (board[i][j]=='K'):
                print i,j
                kings+={"K":(i,j)}
            if (board[i][j]=='k'):
                print i,j    
                kings+={"k":(i,j)}
            j=j+1    
        i=i+1        
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
    kings=find_kings(board)
    i=0
    j=0
    while(i<len(board)):
        while(j<8):
            if (board[i][j]=='P'):
                print i,j
                kings+={"P":(i,j)}
            if (board[i][j]=='p'):
                print i,j    
                kings+={"p":(i,j)}
            j=j+1    
        i=i+1        
    for key in kings:
        if (key=="k"):
            attacker="P"
        if (key=="K"):
            attacker="p"    
    for key in kings:
        if(key=="P"):
            if(kings[key][0]+1<8 and kings["k"][0]==kings[key][0]+1   and kings[key][1]+1<8 and kings["k"][1]==kings[key][1]+1 or kings["k"][1]==kings[key][1]-1):
                check=(("k",attacker,kings[key][0],kings[key][1]))
            
        
                       
    for key in kings:
        if(key=="p"):
            if(kings[key][0]+1<8 and kings["K"][0]==kings[key][0]+1 and kings[key][1]+1<8 and kings["K"][1]==kings[key][1]+1 or kings["K"][1]==kings[key][1]-1):
                check=(("K",attacker,kings[key][0],kings[key][1]))
                    
                           
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
    kings=find_kings(board)
    i=0
    j=0
    while(i<len(board)):
        while(j<8):
            if (board[i][j]=='N'):
                print i,j
                kings+={"N":(i,j)}
            if (board[i][j]=='n'):
                print i,j    
                kings+={"n":(i,j)}
            j=j+1    
        i=i+1        
    for key in kings:
        if (key=="k"):
            attacker="N"
        if (key=="K"):
            attacker="n"
    for key in kings:
        if (key=="n"):
            i=-7
            k=1
            while(i<8 and k==1 ):
                if ((kings["K"][0]==kings[key][0]+i)  and (kings["K"][1]==kings[key][1]+i)):
                    check=("K",attacker,kings[key][0],kings[key][1])
                    k=legal_pos(kings[key][0]+i,kings[key][1]+i) 
                    i=i+1    
    for key in kings:
        if (key=="N"):
            i=-7
            k=1
            while(i<8 and k==1 ):
                if ((kings["k"][0]==kings[key][0]+i)  and (kings["k"][1]==kings[key][1]+i)):
                    check=("k",attacker,kings[key][0],kings[key][1])
                    k=legal_pos(kings[key][0]+i,kings[key][1]+i) 
                    i=i+1                    
                    
               
    
        
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
    king_pos = {}
    k=0
    i=0
    j=0
    while(i<len(board)):
        while(j<8):
            if (board[i][j]=='P'):
                print i,j
                king_pos+={"P":(i,j)}
            if (board[i][j]=='p'):
                print i,j    
                king_pos+={"p":(i,j)}
            j=j+1    
        i=i+1        
    
    
    kings=find_kings(board)
    u=check_pawn_attack(board, k, king_pos)
    king_pos = {}
    i=0
    j=0
    while(i<len(board)):
        while(j<8):
            if (board[i][j]=='N'):
                print i,j
                king_pos+={"N":(i,j)}
            if (board[i][j]=='n'):
                print i,j    
                king_pos+={"n":(i,j)}
            j=j+1    
        i=i+1      
    j=check_knight_attack(board, k, king_pos)
    i=0
    f=0
    for key in kings:
        if (key=="K"):
            while (i<len(board)):
                while(f<8):
                    if (u!=None and j!=None and board(kings[key][0]+1,kings[key][1]+1)!=" " and board(kings[key][0]-1,kings[key][1]-1)!=" " and board(kings[key][0]+1,kings[key][1]-1)!=" " and board(kings[key][0]-1,kings[key][1]+1)!=" "):
                        check=1
                        f=f+1
                i=i+1  
    for key in kings:
        if (key=="k"):
            while (i<len(board)):
                while(f<8):
                    if (u!=None and j!=None and board(kings[key][0]+1,kings[key][1]+1)!=" " and board(kings[key][0]-1,kings[key][1]-1)!=" " and board(kings[key][0]+1,kings[key][1]-1)!=" " and board(kings[key][0]-1,kings[key][1]+1)!=" "):
                        check=1
                        f=f+1
                i=i+1                  
               
    return check

x=raw_input("enter 1st thing")
l0=x.split() 
x=raw_input("enter 2nd thing")
l1=x.split() 
x=raw_input("enter 3rd thing")
l2=x.split() 
x=raw_input("enter 4th thing")
l3=x.split() 
x=raw_input("enter 5th thing")
l4=x.split() 
x=raw_input("enter 6th thing")
l5=x.split() 
x=raw_input("enter 7th thing")
l6=x.split() 
x=raw_input("enter 8th thing")
l7=x.split() 

board=[l0,l1,l2,l3,l4,l5,l6,l7]
k=check_check(board)
if (k==1):
    print"check mate"
else:
    print"not check-mate"    

       


                    
if __name__ == '__main__':
    pass