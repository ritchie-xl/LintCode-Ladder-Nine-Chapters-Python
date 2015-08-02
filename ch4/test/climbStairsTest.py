__author__ = 'lei'

import unittest
from ch4.climb_stairs import climbStairs_2 as cs


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(cs(3), 3)

    def test_2(self):
        self.assertEqual(cs(39), 102334155)

if __name__ == '__main__':
    unittest.main()
