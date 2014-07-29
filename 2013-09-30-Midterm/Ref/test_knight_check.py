import unittest
from testgenDecorator import for_examples
from checkChessCheck import check_check, check_knight_attack, find_kings, check_pawn_attack

class TestChessCheck(unittest.TestCase):

    @for_examples(([['.','.','.','r','k','b','.','r'],
                    ['.','.','N','.','.','p','p','.'],
                    ['p','.','P','p','.','.','.','p'],
                    ['.','p','n','.','.','P','.','.'],
                    ['.','.','.','.','.','.','.','.'],
                    ['.','.','.','.','P','.','.','.'],
                    ['P','.','.','.','.','.','P','P'],
                    ['R','.','.','.','.','R','K','.']], (0,4), (7,6), ('k','N', 1, 2)),

                  ([['.','.','.','.','.','.','.','.'],
                    ['.','.','.','k','.','.','.','.'],
                    ['.','p','n','.','p','.','.','.'],
                    ['.','p','.','.','P','p','.','.'],
                    ['.','.','.','K','.','P','.','.'],
                    ['.','R','.','.','.','.','.','R'],
                    ['P','P','.','.','.','.','.','.'],
                    ['.','.','B','.','.','.','.','.']], (1,3), (4,3), ('K','n', 2, 2)))
                    
    def test_knight_check(self, board, black_king, white_king, knight_check):
        '''
        Test for knight checks
        '''
        kings = find_kings(board)
        self.assertEqual(kings['k'], black_king)
        self.assertEqual(kings['K'], white_king)
        check = check_check(board)
        self.assertEqual(check, knight_check)

if __name__ == "__main__":
    unittest.main()
