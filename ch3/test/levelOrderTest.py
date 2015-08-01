__author__ = 'lei'

import unittest
from ch3.node import TreeNode
import ch3.levelOrderTraverse as lot


class MyTestCase(unittest.TestCase):
    def test_1(self):
        a = TreeNode(1)
        b = TreeNode(2)
        c = TreeNode(3)
        a.left = b
        a.right = c

        self.assertEqual(lot.levelOrder(a), [[1],[2,3]])

    def test_1(self):
        a = TreeNode(1)
        b = TreeNode(2)
        c = TreeNode(3)
        d = TreeNode(4)
        e = TreeNode(5)
        a.left = b
        a.right = c
        c.left = d
        c.right = e

        self.assertEqual(lot.levelOrder(a), [[1],[2,3],[4,5]])

if __name__ == '__main__':
    unittest.main()
