__author__ = 'Lei Xia'

import unittest
from ch4.jump_game import canJump as cj
from ch4.jump_gameII import jump


class MyTestCase(unittest.TestCase):
    def test_1(self):
        A = [2,3,1,1,4]
        self.assertEqual(cj(A), True)

    def test_2(self):
        A = [3,2,1,0,4]
        self.assertEquals(cj(A), False)

    def test_3(self):
        A = [2,3,1,1,4]
        self.assertEquals(jump(A),2)

    def test_4(self):
        A = [13,52,42,21,58]
        self.assertEquals(jump(A),1)

    def test_5(self):
        A = [17,8,29,17,35,28,14,2,45,8,6,54,24,43,20,14,33,31,27,11]
        self.assertEquals(jump(A),2)

    def test_6(self):
        A = [10,9,32,8,7,56,5,5,44,14,30,37,1,50,40,19,77,42,1,27]
        self.assertEquals(jump(A),2)


if __name__ == '__main__':
    unittest.main()
