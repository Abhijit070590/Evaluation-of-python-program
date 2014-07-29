
def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    kings = {}
    for x in range(0,8):
        for i in range(0,8}:
            if(board[x][i]=='k'):
                kings['k']=[x,i]
            if(board[x][i]=='K'):
                kings['K']=[x,i]
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
    x=king_pos[0]
    y=king_pos[1]
    ''' You code comes here '''
    if(k=='k'):
        if(board[x+1][y+1]=='P'):
            check={k,'P',x+1,y+1}
        elif(board[x+1][y-1]=='P'):
            check={k,'P',x+1,y-1}
    elif(k=='K'):
        if(board[x-1][y+1]=='p'):
            check={k,'p',x-1,y+1}
        elif(board[x-1][y-1]=='p'):
            check={k,'p',x-1,y-1}
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
    x=king_pos[0]
    y=king_pos[1]
    ''' You code comes here '''
    if(k=='k'):
        if(board[x+1][y+2]=='N'):
              check={k,'N',x,y}
        elif(board[x+2][y+1]=='N'):
              check={k,'N',x+2,y+1}
        elif(board[x+1][y-2]=='N'):
              check={k,'N',x+1,y-2}
        elif(board[x+2][y-1]=='N'):
              check={k,'N',x+2,y-1}
        elif(board[x-1][y+2]=='N'):
              check={k,'N',x-1,y+2}
        elif(board[x-2][y+1]=='N'):
              check={k,'N',x-2,y+1}
        elif(board[x-1][y-2]=='N'):
              check={k,'N',x-1,y-2}
        elif(board[x-2][y-1]=='N'):
              check={k,'N',x-2,y-1}
    elif(k=='K'):
          if(board[x+1][y+2]=='n'):
              check={k,'n',x+1,y+2}
          elif(board[x+2][y+1]=='n'):
              check={k,'n',x+2,y+1} 
          elif(board[x+1][y-2]=='n'):
              check={k,'n',x+1,y-2}
          elif(board[x+2][y-1]=='n'):
              check={k,'n',x+2,y-1} 
          elif(board[x-1][y+2]=='n'):
              check={k,'n',x-1,y+2}
          elif(board[x-2][y+1]=='n'):
              check={k,'n',x-2,y+1}
          elif(board[x-1][y-2]=='n'):
              check={k,'n',x-1,y-2}
          elif(board[x-2,y-1]=='n'):
              check={k,'n',x-2,y-1}
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
    kings=find_kings(board)
    check=check_pawn_attack(board,'k',kings['k'])
    if(check==None):
        check=check_pawn_attack(board,'K',kings['K'])
    if(check==None):
        check=check_knight_attack(board,'k',kings['k'])
    if(check==None):
        check=check_knight_attack(board,'K',kings['K'])
    '''Checking for Rook and Queen for Black King'''
    if(check==None):
        king_pos=kings['k']
        k='k'
        x=king_pos[0]
        y=king_pos[1]
        while(1):
            if(board[x+0][y+1]=='Q'):
                check={k,'Q',x,y+1}
                break
            elif(board[x+0][y+1]=='R'):
                check={k,'R',x,y+1}
                break
            elif(board[x+0][y+1]!='R'):
                if(board[x+0][y+1]!='Q'):
                    break
        while(1):      
            if(board[x+0][y-1]=='Q'):
                check={k,'Q',x,y-1}
                break
            elif(board[x+0][y-1]=='R'):
                check={k,'R',x,y-1}
                break
            elif(board[x+0][y-1]!='R'):
                if(board[x+0][y-1]!='Q'):
                    break
        while(1):
            if(board[x+1][y+0]=='Q'):
                check={k,'Q',x+1,y} 
                break
            elif(board[x+1][y+0]=='R'):
                check={k,'R',x+1,y}
                break
            elif(board[x+1][y]!='R'):
                if(board[x+1][y]!='Q'):
                    break
        while(1):
            if(board[x-1][y+0]=='Q'):
                check={k,'Q',x-1,y}
                break
            elif(board[x-1][y+0]=='R'):
                check={k,'R',x-1,y}
                break
            elif(board[x-1][y]!='R'):
                if(board[x-1][y]!='Q'):
                    break
                
    '''Checking for Rook and Queen for White King'''
    if(check==None):
        king_pos=kings['K']
        k='K'
        x=king_pos[0]
        y=king_pos[1]
        while(1):
            if(board[x+0][y+1]=='q'):
                check={k,'q',x,y+1}
                break
            elif(board[x+0][y+1]=='r'):
                check={k,'r',x,y+1}
                break
            elif(board[x+0][y+1]!='r'):
                if(board[x+0][y+1]!='q'):
                    break
        while(1):      
            if(board[x+0][y-1]=='q'):
                check={k,'q',x,y-1}
                break
            elif(board[x+0][y-1]=='r'):
                check={k,'r',x,y-1}
                break
            elif(board[x+0][y-1]!='r'):
                if(board[x+0][y-1]!='q'):
                   break
        while(1):
            if(board[x+1][y+0]=='q'):
                check={k,'q',x+1,y}
                break
            elif(board[x+1][y+0]=='r'):
                check={k,'r',x+1,y}
                break
            elif(board[x+1][y]!='r'):
                if(board[x+1][y]!='q'):
                    break
        while(1):
            if(board[x-1][y+0]=='q'):
                check={k,'q',x-1,y}
                break
            elif(board[x-1][y+0]=='r'):
                check={k,'r',x-1,y}
                break
            elif(board[x-1][y]!='r'):
                if(board[x-1][y]!='q'):
                    break     
    
    '''Checking for Bishop and Queen for Black King'''  
    if(check==None):
        king_pos=kings['k']
        k='k'
        x=king_pos[0]
        y=king_pos[1]
        while(1):
            if(board[x+1][y+1]=='Q'):
                check={k,'Q',x+1,y+1}
                break
            elif(board[x+1][y+1]=='B'):
                check={k,'B',x+1,y+1}
                break
            elif(board[x+1][y+1]!='B'):
                if(board[x+1][y+1]!='Q'):
                    break
        while(1):      
            if(board[x+1][y-1]=='Q'):
                check={k,'Q',x+1,y-1}
                break
            elif(board[x+1][y-1]=='B'):
                check={k,'B',x,y-1}
                break
            elif(board[x+1][y-1]!='B'):
                if(board[x+1][y-1]!='Q'):
                    break
        while(1):
            if(board[x-1][y-1]=='Q'):
                check={k,'Q',x-1,y-1}
                break
            elif(board[x-1][y-1]=='B'):
                check={k,'B',x-1,y-1}
                break
            elif(board[x-1][y-1]!='B'):
                if(board[x-1][y-1]!='Q'):
                     break
        while(1):
            if(board[x-1][y+1]=='Q'):
                check={k,'Q',x-1,y+1}
                break
            elif(board[x-1][y+1]=='B'):
                check={k,'B',x-1,y+1}
                break
            elif(board[x-1][y+1]!='B'):
                if(board[x-1][y+1]!='Q'):
                    break
    '''Checking for Bishop and Queen for White King'''  
    if(check==None):
        king_pos=kings['K']
        k='K'
        x=king_pos[0]
        y=king_pos[1]
        while(1):
            if(board[x+1][y+1]=='q'):
                check={k,'q',x+1,y+1}
                break
            elif(board[x+1][y+1]=='b'):
                check={k,'b',x+1,y+1}
                break
            elif(board[x+1][y+1]!='b'):
                if(board[x+1][y+1]!='q'):
                   break
        while(1):      
            
            if(board[x+1][y-1]=='q'):
                check={k,'q',x+1,y-1}
                break
            elif(board[x+1][y-1]=='b'):
                check={k,'b',x,y-1}
                break
            elif(board[x+1][y-1]!='b'):
                if(board[x+1][y-1]!='q'):
                   break
        while(1):
            
            if(board[x-1][y-1]=='q'):
                check={k,'q',x-1,y-1}
                break
            elif(board[x-1][y-1]=='b'):
                check={k,'b',x-1,y-1}
                break
            elif(board[x-1][y-1]!='b'):
                if(board[x-1][y-1]!='q'):
                    break
        while(1):
            if(board[x-1][y+1]=='q'):
                check={k,'q',x-1,y+1}
                break
            elif(board[x-1][y+1]=='b'):
                check={k,'b',x-1,y+1}
                break
            elif(board[x-1][y+1]!='b'):
                if(board[x-1][y+1]!='q'):
                     break
    
    ''' You code comes here '''
        
    return check
                    
if __name__ == '__main__':
    pass

