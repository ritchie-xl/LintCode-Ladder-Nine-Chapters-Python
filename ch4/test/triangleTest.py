__author__ = 'Lei Xia'

import unittest
from ch4.triangle_1 import minimumTotal as mt1


class MyTestCase(unittest.TestCase):
    def test_1(self):
        a = [
                   [2],
                  [3,4],
                 [6,5,7],
                [4,1,8,3]
             ]
        self.assertEqual(mt1(a), 11)


if __name__ == '__main__':
    unittest.main()
