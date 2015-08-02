__author__ = 'Lei Xia'

import unittest
from ch4.triangle import minimumTotal as mt

class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = [
                   [2],
                  [3,4],
                 [6,5,7],
                [4,1,8,3]
             ]
        self.assertEqual(mt(a), 11)


if __name__ == '__main__':
    unittest.main()
