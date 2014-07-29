'''
Created on 29-Sep-2013

@author: Raghavan
'''

ROW_COL_RANGE = range(8)

def is_legal(row, col):
    '''
    Checks if a given board position with row and col is a valid board position
    '''
    return (row in ROW_COL_RANGE and col in ROW_COL_RANGE)

def is_piece_attacker(king, piece):
    return ((king.isupper() and piece.islower()) or (king.islower() and piece.isupper()))

def find_kings(board):
    '''
    Find the positions of the two kings
    return a hash that has a tuple (x,y) associated with 'k' and 'K' (black and white kings) respectively
    '''
    kings = {}
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if (piece == 'k' or piece == 'K'):
                kings[piece] = (i, j)
                if (kings.has_key('k') and kings.has_key('K')):
                    # stop searching further after we have found both the kings
                    return kings
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
    pawn_row = (1 if (k == 'k') else -1) + king_pos[0]
    for pawn_col in [(king_pos[1] + 1), (king_pos[1] - 1)]:
        if is_legal(pawn_row, pawn_col):
            piece = board[pawn_row][pawn_col]
            if (is_piece_attacker(k, piece) and (piece.lower() == 'p')):
                return (k, piece, pawn_row, pawn_col)
    return None


def check_knight_attack(board, k, king_pos):
    '''
    Check if the king (argument k - it is 'k' if it is black king and 'K' for white king) at position king_pos
    - king_pos is a tuple (row, col) - is being attacked by a opposite color knight
    check positions (+/- 1, +/- 2), (+/- 2, +/- 1) away from king_pos and see if any of them is a opposite color knight
    You need to of course first check that these are legal board positions
    Return a tuple (k, attacker, attacker_x, attacker_y) - attacker will be 'N' or 'n' depending on
    whether k is 'k' or 'K' - if the king is under check, else return None
    '''
    krow, kcol = king_pos[0], king_pos[1]
    for row_inc in [1, 2]:
        col_inc = 3 - row_inc
        for knight_pos in [((krow + row_inc), (kcol + col_inc)), ((krow - row_inc), (kcol + col_inc)),
                           ((krow + row_inc), (kcol - col_inc)), ((krow - row_inc), (kcol - col_inc))]:
            # Loop through every possible knight position relative to the king
            nrow, ncol = knight_pos[0], knight_pos[1]
            if is_legal(nrow, ncol): # make sure it is a legal board position
                attacker = board[nrow][ncol]
                # see if the piece (if any) on the board is the opposite colour knight
                if (is_piece_attacker(k, attacker) and (attacker.lower() == 'n')):
                    return (k, attacker, nrow, ncol)
    return None


def is_diagonal(direction):
    '''
    Return true if the x and y increments represent a movement along a diagonal
    '''
    return (direction[0] != 0 and direction[1] != 0)
    
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
    kings = find_kings(board) # Find the positions of both the kings
    for k in ['k', 'K']:
        # Depending on the king for which we are finding if it is under check
        # change the case OPP_PIECES to indicate the correct opposite color piece

        king_pos = kings[k] # Get the position of the current king
        check = check_pawn_attack(board, k, king_pos)
        if (check != None):
            return check
        check =  check_knight_attack(board, k, king_pos)
        if (check != None):
            return check

        for direction in [ (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1) ]:
            # Look in all 8 directions from which checks could happen
            # new_x, new_y is the position after a move in the chosen direction
            # notice that this is cumulative - as one keeps moving in the same direction
            new_row = king_pos[0] + direction[0]
            new_col = king_pos[1] + direction[1]
            while is_legal(new_row, new_col): # check if the new position is a valid board position
                piece = board[new_row][new_col]
                piece_type = piece.lower()
                if (piece == '.'):
                    # if the board is not occupied at the new position - continue moving in the same direction
                    new_row += direction[0]
                    new_col += direction[1]
                elif (is_piece_attacker(k, piece) and
                      ((piece_type == 'q') or
                       ((not is_diagonal(direction)) and (piece_type == 'r')) or
                       (is_diagonal(direction) and (piece_type == 'b')))):
                    # if the piece is a queen or diagonal bishop or a vert/horizontal rook then declare check
                    return (k, piece, new_row, new_col)
                else:
                    # if the king is blocked by any other piece
                    # then - stop searching in that direction for a check - the king has been blocked from attackers
                    break

    return None
                    
if __name__ == '__main__':
    pass