__author__ = 'Lei Xia'

import unittest
from ch3.node import  TreeNode
import ch3.BST_Iterator as bi


class MyTestCase(unittest.TestCase):

    def test_something(self):
        a = TreeNode(2)
        b = TreeNode(1)
        a.left = b

        c = bi.Solution(a)
        self.res = []
        while c.hasNext():
            self.res.append(c.next())

        self.assertEqual(self.res, [1,2])


if __name__ == '__main__':
    unittest.main()
