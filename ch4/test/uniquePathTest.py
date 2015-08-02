__author__ = 'lei'

import unittest
from ch4.Unique_Path import uniquePaths as up
from ch4.unique_path_2 import uniquePathsWithObstacles as up2


class MyTestCase(unittest.TestCase):
    def test_1(self):
        m = 2
        n =3
        self.assertEqual(up(2,3), 3)

    def test_2(self):
        a = [
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ]
        self.assertEqual(up2(a),2)

    def test_3(self):
        a = [
         [0]
        ]
        self.assertEqual(up2(a),1)

    def test_4(self):
        a = [[0,0],[0,0],[0,0],[1,0],[0,0]]
        self.assertEqual(up2(a),3)


    def test_5(self):
        a =[[1,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.assertEqual(up2(a),0)

if __name__ == '__main__':
    unittest.main()
