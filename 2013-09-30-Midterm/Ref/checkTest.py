import unittest
from testgenDecorator import for_examples
from checkChessCheck_ref import check_check, check_knight_attack, find_kings, check_pawn_attack

class TestChessCheck(unittest.TestCase):

    @for_examples(([['r','n','b','q','k','b','n','r'],
                    ['p','p','p','p','p','p','p','p'],
                    ['.','.','.','.','.','.','.','.'],
                    ['.','.','.','.','.','.','.','.'],
                    ['.','.','.','.','.','.','.','.'],
                    ['.','.','.','.','.','.','.','.'],
                    ['P','P','P','P','P','P','P','P'],
                    ['R','N','B','Q','K','B','N','R']], (0,4), (7,4), None),

                  ([['r','.','b','q','k','b','n','r'],
                    ['p','p','p','p','.','p','p','p'],
                    ['.','.','n','.','.','.','.','.'],
                    ['.','.','.','.','p','.','.','.'],
                    ['.','.','.','.','P','.','.','.'],
                    ['.','.','.','.','.','N','.','.'],
                    ['P','P','P','P','.','P','P','P'],
                    ['R','N','B','Q','K','B','.','R']], (0,4), (7,4), None))
    def testNoCheck(self, board, black_king, white_king, no_check):
        '''
        Test for knight checks
        '''
        kings = find_kings(board)
        self.assertEqual(kings['k'], black_king)
        self.assertEqual(kings['K'], white_king)
        check = check_check(board)
        self.assertEqual(check, no_check)

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
    def testKnightCheck(self, board, black_king, white_king, knight_check):
        '''
        Test for knight checks
        '''
        kings = find_kings(board)
        self.assertEqual(kings['k'], black_king)
        self.assertEqual(kings['K'], white_king)
        check = check_check(board)
        self.assertEqual(check, knight_check)

    @for_examples(([['r','n','b','q','.','b','n','r'],
                    ['p','p','p','p','p','.','.','.'],
                    ['.','.','.','.','.','.','p','.'],
                    ['.','.','.','.','.','.','.','k'],
                    ['.','.','.','.','.','Q','P','p'],
                    ['.','.','.','.','P','.','.','.'],
                    ['P','P','P','P','.','P','.','P'],
                    ['R','N','B','.','K','.','N','R']], (3,7), (7,4), ('k','P', 4, 6)))
    def testPawnCheck(self, board, black_king, white_king, pawn_check):
        '''
        Test for knight checks
        '''
        kings = find_kings(board)
        self.assertEqual(kings['k'], black_king)
        self.assertEqual(kings['K'], white_king)
        check = check_check(board)
        self.assertEqual(check, pawn_check)

    @for_examples(([['r','n','.','.','b','r','k','.'],
                    ['.','.','.','.','.','p','p','p'],
                    ['.','.','p','.','p','.','.','.'],
                    ['p','p','q','P','.','.','.','.'],
                    ['P','n','p','.','P','.','N','.'],
                    ['N','.','.','.','.','P','P','.'],
                    ['.','P','.','Q','.','.','B','P'],
                    ['R','.','.','R','.','.','K','.']], (0,6), (7,6), ('K','q', 3, 2)))
    def testQueenCheck(self, board, black_king, white_king, queen_check):
        '''
        Test for knight checks
        '''
        kings = find_kings(board)
        self.assertEqual(kings['k'], black_king)
        self.assertEqual(kings['K'], white_king)
        check = check_check(board)
        self.assertEqual(check, queen_check)

if __name__ == "__main__":
    unittest.main()