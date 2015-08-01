__author__ = 'lei'

import unittest
from ch3.node import TreeNode
import ch3.LCAonBT as lca


class MyTestCase(unittest.TestCase):

    def test_something(self):
        a = TreeNode(1)
        self.assertEqual(lca.lowestCommonAncestor(a,1,1).val, 1)

if __name__ == '__main__':
    unittest.main()
