
def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    kings = {}
        
    ''' Your code comes here '''
    
    i=0
    j=0
    while(i<=7):
        j=0
        while(j<=7):
            if(board[i][j]=='k'):
                kings['k']=(i,j)
            elif(board[i][j]=='K'):
                kings['K']=(i,j)
                
            j+=1
        
        i+=1
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
    
    ''' You code comes here '''
    
    
    king_pos_row=king_pos[0]
    king_pos_clmn=king_pos[1]
       
    if(king_pos_row<0 or king_pos_row>7 or king_pos_clmn<0 or king_pos_clmn>7):
        print "invalid position"
        exit(0) 
    
    i,j=0,0                                         
    if(k=='k'):
        while(i<=7):
            j=0
            while(j<=7):
                if(board[i][j]=='P'):
                    if((i==(king_pos_row+1)) and ((j==(king_pos_clmn+1)) or (j==(king_pos_clmn-1)))):
                        check=(k,'P',i,j)
                        print check
                        exit(0)
                
                
                j+=1
                
                
            i+=1
            
           
                 
    if(k=='K'):
        while(i<=7):
            j=0
            while(j<=7):
                if(board[i][j]=='p'):
                    if((i==(king_pos_row-1)) and ((j==(king_pos_clmn+1)) or (j==(king_pos_clmn-1)))):
                        check=(k,'p',i,j)
                        print check
                        exit(0)
                
                j+=1
                
            i+=1
                                    
    
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
     
    king_pos_row=king_pos[0]
    king_pos_clmn=king_pos[1]
    print king_pos_row, king_pos_clmn
    
    
    if(king_pos_row<0 or king_pos_row>7 or king_pos_clmn<0 or king_pos_clmn>7):# or (king_pos_row-2)<0 or (king_pos_row+2)>7 (king_pos_clmn-2)<0 or (king_pos_clmn+2)>7):
        print "invalid position"
        exit(0) 
    
    i,j=0,0                                         
    if(k=='k'):
        while(i<=7):
            j=0
            while(j<=7):
                if(board[i][j]=='N'):
                    if((i==(king_pos_row+1)  and j==(king_pos_clmn+2)) or (i==(king_pos_row-1)  and j==(king_pos_clmn-2)) or (i==(king_pos_row+1)  and j==(king_pos_clmn-2)) or (i==(king_pos_row-1)  and j==(king_pos_clmn+2)) or (i==(king_pos_row+2)  and j==(king_pos_clmn+1)) or (i==(king_pos_row-2)  and j==(king_pos_clmn-1)) or (i==(king_pos_row-2)  and j==(king_pos_clmn+1)) or (i==(king_pos_row+2)  and j==(king_pos_clmn-1))):
                        check=(k,'N',i,j)
                        print check
                        exit(0)
                        
                j+=1
                
            i+=1                       
            
    elif(k=='K'):
        while(i<=7):
            j=0
            while(j<=7):
                if(board[i][j]=='n'):
                    if((i==(king_pos_row+1)  and j==(king_pos_clmn+2)) or 
                       (i==(king_pos_row-1)  and j==(king_pos_clmn-2)) or 
                       (i==(king_pos_row+1)  and j==(king_pos_clmn-2)) or 
                       (i==(king_pos_row-1)  and j==(king_pos_clmn+2)) or 
                       (i==(king_pos_row+2)  and j==(king_pos_clmn+1)) or 
                       (i==(king_pos_row-2)  and j==(king_pos_clmn-1)) or 
                       (i==(king_pos_row-2)  and j==(king_pos_clmn+1)) or 
                       (i==(king_pos_row+2)  and j==(king_pos_clmn-1))):
                        check=(k,'n',i,j)
                        print check
                        exit(0)
                        
                
                j+=1
                
            i+=1
                                         
             
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
    
    
    kings=find_kings(board)
    
    check_pawn_attack(board,'k',kings['k'])
    check_pawn_attack(board,'K',kings['K'])
    check_knight_attack(board,'k',kings['k'])
    check_knight_attack(board,'K',kings['K'])
    
    if(check!=None):
        return check    
    
    t=kings['k']
    king_pos_row=t[0]
    king_pos_clmn=t[1]
    
    i,j=0,0
    
       
    while(i<=7):
            j=0
            while(j<=7):
                if(board[i][j]=='Q' or board[i][j]=='R' ):
                    if((i==(king_pos_row) and (j==(king_pos_clmn+1))) or (i==(king_pos_row) and (j==(king_pos_clmn-1))) or (i==(king_pos_row+1) and (j==(king_pos_clmn))) or (i==(king_pos_row-1) and (j==(king_pos_clmn)))):
                        if(board[i][j]=='Q'):
                            check=('k','Q',i,j)
                            print check
                            exit(0)
                        else:
                            check=('k','R',i,j)
                            print check
                            exit(0)
                        
                        flag=1
                        break
                    elif((i==(king_pos_row+1) and (j==(king_pos_clmn+1))) or (i==(king_pos_row-1) and (j==(king_pos_clmn-1))) or (i==(king_pos_row+1) and (j==(king_pos_clmn-1))) or (i==(king_pos_row-1) and (j==(king_pos_clmn+1)))):
                         if(board[i][j]=='Q'):
                            check=('k','Q',i,j)
                            print check
                            exit(0)
                         else:
                            check=('k','B',i,j)
                            print check
                            exit(0)
                                                                  
                    
                j+=1
                
            i+=1
           
    
    if(check!=None):
        return check
    
    t=kings['K']
    king_pos_row=t[0]
    king_pos_clmn=t[1]
    
    i,j=0,0
    
    while(i<=7):
            j=0
            while(j<=7):
                if(board[i][j]=='q' or board[i][j]=='r' ):
                    if((i==(king_pos_row) and (j==(king_pos_clmn+1))) or (i==(king_pos_row) and (j==(king_pos_clmn-1))) or (i==(king_pos_row+1) and (j==(king_pos_clmn))) or (i==(king_pos_row-1) and (j==(king_pos_clmn)))):
                        if(board[i][j]=='q'):
                            check=('K','q',i,j)
                            print check
                            exit(0)
                        else:
                            check=('K','r',i,j)
                            print check
                            exit(0)
                        
                     
                    
                    elif((i==(king_pos_row+1) and (j==(king_pos_clmn+1))) or (i==(king_pos_row-1) and (j==(king_pos_clmn-1))) or (i==(king_pos_row+1) and (j==(king_pos_clmn-1))) or (i==(king_pos_row-1) and (j==(king_pos_clmn+1)))):
                         if(board[i][j]=='Q'):
                             check=('K','Q',i,j)
                             print check
                             exit(0)
                         else:
                             check=('K','B',i,j)
                             print check
                             exit(0)
                j+=1
                
            i+=1
            
    
        
    
    
    
                    
if __name__ == '__main__':
    board=[]
    board=raw_input("")
    check_check(board)
    
    
