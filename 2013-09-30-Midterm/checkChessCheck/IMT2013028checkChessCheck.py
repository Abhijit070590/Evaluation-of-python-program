chess=[]
check_posn=[]
coin=""
check=0

def check_for_check(count1,count2,white):
        if((white==1 and chess[count1][count2].islower()) or (white==0 and chess[count1][count2].isupper())):
            check_posn.append(count1)
            check_posn.append(count2)
            coin=chess[count1][count2]
            return 1
        return 0
    
def ischeck(coin_pos,white):
        check=0
        
        # Check for Check by bishop
        count1=coin_pos[0]
        count3=coin_pos[0]
        count2=coin_pos[1]
        count4=coin_pos[1]
        while(count1<8 and count2 < 8):
            count1+=1
            count3-=1
            count2+=1
            count4-=1
            if(chess[count1][count2]=="b" or chess[count1][count2]=="B" or chess[count1][count2]=="q" or chess[count1][count2]=="Q"):
                if(check_for_check(count1,count2,white) or check_for_check(count3,count2,white) or check_for_check(count1,count4,white) or check_for_check(count3,count4,white)):
                    check=1
            elif(chess[count1][count2]!="."):
                check=0
                break
        
        # Check for Check by rook    
        count1=coin_pos[0]
        count3=coin_pos[0]
        count2=coin_pos[1]
        count4=coin_pos[1]
        while(count1<8 and count2 < 8):
            count1+=1
            count3-=1
            count2+=1
            count4-=1
            if(chess[count1][coin_pos[1]]=="r" or chess[coin_pos[0]][count2]=="R" or chess[count3][coin_pos[1]]=="q" or chess[coin_pos[0]][count4]=="Q"):
                if(check_for_check(count1,coin_pos[1],white) or check_for_check(coin_pos[0],count2,white) or check_for_check(count3,coin_pos[1],white) or check_for_check(coin_pos[0],count4,white)):
                    check=1
            elif(chess[count1][count2]!="."):
                check=0
                break
        
        # Check for CHECK by pawn
        if(coin_pos[1]-1 >=0):
            if(coin_pos[0]-1 >=0):
                if(chess[coin_pos[0]-1][coin_pos[1]-1]=="p" and white==1):
                    check=1
                    coin='p'
            elif(coin_pos[0]+1 < 8):
                if(chess[coin_pos[0]+1][coin_pos[1]-1]=="p" and white==1):
                    check=1
                    coin='p'
        if(coin_pos[1]+1 <8):
            if(coin_pos[0]-1 >=0):
                if(chess[coin_pos[0]-1][coin_pos[1]+1]=="P" and white==0):
                    check=1
                    coin='P'
            elif(coin_pos[0]+1 < 8):
                if(chess[coin_pos[0]+1][coin_pos[1]+1]=="P" and white==0):
                    check=1
                    coin='P'
        return check

def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    i=0
    bking=[]
    wking=[]
    while(i<8):
        j=0
        while(j<8):
            if(board[i][j]=="k"):
                bking=[i,j]
            elif(board[i][j]=="K"):
                wking=[i,j]
            j+=1
        i+=1
    chess=board[:]
    printtuple=()
      
    if(ischeck(bking,0)):
        printtuple.append(("black",check_posn,coin))
        print printtuple(0)
    elif(ischeck(wking,1)):
        printtuple.append(("white",check_posn,coin))
        print printtuple(0)
    else:
        print("none")
        
    return 1

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
    - king_pos is a tupls):e (row, col) - is being attacked by a opposite color knight
    check positions (+/- 1, +/- 2), (+/- 2, +/- 1) away from king_pos and see if any of them is a opposite color knight
    You need to of course first check that these are legal board positions
    Return a tuple (k, attacker, attacker_x, attacker_y) - attacker will be 'N' or 'n' depending on
    whether k is 'k' or 'K' - if the king is under check, else return None
    '''
    check = None
     
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
