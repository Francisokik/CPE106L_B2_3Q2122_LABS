import unittest

class WinningMoveTestCase(unittest.TestCase):

    def testMove1(self): # test method name begin with 'test'
        win_move = '0,1,3'
        self.assertEqual(win_move, '0,1,3')
    def testMove2(self): 
        win_move2 = '3,4,5'
        self.assertEqual(win_move2, '3,4,5')
    def testMove3(self): 
        win_move3 = '6,7,8'
        self.assertEqual(win_move3, '6,7,8')
    def testMove4(self): 
        win_move4 = '0,3,6'
        self.assertEqual(win_move4, '0,3,6')
    def testMove5(self): 
        win_move5 = '1,4,7'
        self.assertEqual(win_move5, '1,4,7')
    def testMove6(self): 
        win_move6 = '2,5,8'
        self.assertEqual(win_move6, '2,5,8')
    def testMove7(self): 
        win_move7 = '0,4,8'
        self.assertEqual(win_move7, '0,4,8')
    def testMove8(self): 
        win_move8 = '2,4,6'
        self.assertEqual(win_move8, '2,4,6')

if __name__ == '__main__':
    unittest.main()
