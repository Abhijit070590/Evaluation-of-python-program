def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    kings = {}
    for row in board:
        for column in row:
            if(column=='k'):
                kings['k']=(row,column)
            if(column=='K'):
                kings['K']=(row,column)
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
    if k=='k':
        i=king_pos[0] 
        j=king_pos[1]
        for row in board:
            if(row==i):
                attacker_x=row
                prev= row-1
                for column in prev:
                        c1=j-1
                        c2=j+1
                        if c1=='P':
                            attacker='p'
                            attacker_y=c1
                        if c2=='p':
                            attacker='p'
                            attacker_y=c2
                            after=row+1
                            for column in row:
                                c1=j-1
                                c2=j+1
                            if c1=='P':
                                attacker='p'
                                attacker_y=c1
                            if c2=='p':
                                attacker='p'
                                attacker_y=c2
        check=(k,attacker,attacker_x,attacker_y)
        if k=='K':
            i=king_pos[0] 
            j=king_pos[1]
            for row in board:
                if(row==i):
                    prev=row-1
                    for column in prev:
                        c1=column-1
                        c2=column+1
                        if c1=='P':
                            attacker='P'
                            attacker_y=c1
                        if c2=='p':
                            attacker='P'
                            attacker_y=c2
                        after=row+1
                        for column in after:
                            c1=column-1
                            c2=column+1
                            if c1=='P':
                                attacker='P'
                                attacker_y=c1
                            if c2=='p':
                                attacker='P'
                                attacker_y=c2
        check=(k,attacker,attacker_x,attacker_y)
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
    knightpos=()
    if k=='k':
        i=king_pos[0] 
        j=king_pos[1]
        for rowk in board:
            for columnk in rowk:
                if columnk=='N':
                    knightpos=(rowk,columnk)
        if cmp((i+1,j+2),knightpos)==0:
            attacker='n'
            attacker_x=rowk
            attacker_y=columnk
        if cmp((i-1,j+2),knightpos)==0:
            attacker='n'
            attacker_x=rowk
            attacker_y=columnk
        if cmp((i+1,j-2),knightpos)==0:
            attacker='n'
            attacker_x=rowk
            attacker_y=columnk
        if cmp((i-1,j-2),knightpos)==0:
            attacker='n'
            attacker_x=rowk
            attacker_y=columnk
        check = (k,attacker,attacker_x,attacker_y)
    if k=='K':
        i=king_pos[0] 
        j=king_pos[1]
        for rowk in board:
            for columnk in rowk:
                if columnk=='n':
                    knightpos=(rowk,columnk)
        if cmp((i+1,j+2),knightpos)==0:
            attacker='N'
            attacker_x=rowk
            attacker_y=columnk
        if cmp((i-1,j+2),knightpos)==0:
            attacker='N'
            attacker_x=rowk
            attacker_y=columnk
        if cmp((i+1,j-2),knightpos)==0:
            attacker='N'
            attacker_x=rowk
            attacker_y=columnk
        if cmp((i-1,j-2),knightpos)==0:
            attacker='N'
            attacker_x=rowk
            attacker_y=columnk
        check = (k,attacker,attacker_x,attacker_y)
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
    kings = {}
    kingpos=()
    for row in board:
        for column in row:
            if(column=='k'):
                kings['k']=(row,column)
            if(column=='K'):
                kings['K']=(row,column)
    kingpos=kings['k']
    pos1=kingpos[0][0]
    pos2=kingpos[0][1]
    for rowr in board:
        for columnr in rowr:
            if columnr=='R':
                rookpos=(rowr,columnr)
    for rowq in board:
        for columnq in rowr:
            if columnq=='Q':
                queenpos=(rowq,columnq)
    if cmp((pos1,pos2+1),rookpos)==0:
            attacker='R'
            attacker_x=rowr
            attacker_y=columnr
    if cmp((pos1,pos2+1),queenpos)==0:
            attacker='Q'
            attacker_x=rowq
            attacker_y=columnq
    if cmp((pos1,pos2-1),rookpos)==0:
            attacker='R'
            attacker_x=rowr
            attacker_y=columnr
    if cmp((pos1,pos2-1),queenpos)==0:
            attacker='Q'
            attacker_x=rowq
            attacker_y=columnq
    if cmp((pos1+1,pos2),rookpos)==0:
            attacker='R'
            attacker_x=rowr
            attacker_y=columnr
    if cmp((pos1+1,pos2),queenpos)==0:
            attacker='Q'
            attacker_x=rowq
            attacker_y=columnq
    if cmp((pos1-1,pos2),rookpos)==0:
            attacker='R'
            attacker_x=rowr
            attacker_y=columnr
    if cmp((pos1-1,pos2),queenpos)==0:
            attacker='Q'
            attacker_x=rowq
            attacker_y=columnq
    check=('k',attacker,attacker_x,attacker_y)
    kingpos=kings['K']
    pos1=kingpos[1][0]
    pos2=kingpos[1][1]
    for rowr in board:
    	for columnr in rowr:
    		if columnr=='R':
    			rookpos=(rowr1,columnr1)
    for rowq in board:
		for columnq in rowq:
			if columnq=='Q':
				queenpos=(rowq,columnq)
	if cmp((pos1,pos2+1),rookpos)==0:
			attacker='R'
			attacker_x=rowr
			attacker_y=columnr
	if cmp((pos1,pos2+1),queenpos)==0:
			attacker='Q'
			attacker_x=rowq
			attacker_y=columnq
	if cmp((pos1,pos2-1),rookpos)==0:
			attacker='R'
			attacker_x=rowr
			attacker_y=columnr
	if cmp((pos1,pos2-1),queenpos)==0:
			attacker='Q'
			attacker_x=rowq
			attacker_y=columnq
	if cmp((pos1+1,pos2),rookpos)==0:
			attacker='R'
			attacker_x=rowr
			attacker_y=columnr
	if cmp((pos1+1,pos2),queenpos)==0:
			attacker='Q'
			attacker_x=rowq
			attacker_y=columnq
	if cmp((pos1-1,pos2),rookpos)==0:
			attacker='R'
			attacker_x=rowr
			attacker_y=columnr
	if cmp((pos1-1,pos2),queenpos)==0:
		attacker='Q'
		attacker_x=rowq
		attacker_y=columnq	
	check('K',attacker,attacker_x,attacker_y)
	return check
    

                    
if __name__ == '__main__':
    pass
