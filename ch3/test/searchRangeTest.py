__author__ = 'lei'

import unittest
from ch3.node import TreeNode as t
import ch3.searchRange as sr


class MyTestCase(unittest.TestCase):
    def test_1(self):
        a = t(2)
        b=t(1)
        a.left = b
        self.assertEqual(sr.searchRange(a,0,4), [1,2])

    def test_2(self):
        a = t(20)
        b = t(1)
        a.left = b
        c = t(40)
        a.right = c
        d = t(35)
        c.left = d
        self.assertEqual(sr.searchRange(a,17,37),[20,35])

if __name__ == '__main__':
    unittest.main()
