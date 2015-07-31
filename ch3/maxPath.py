__author__ = 'lei'
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        maxSum, _ = self.maxPathSumHelper(root)
        return maxSum


    def maxPathSumHelper(self,root):
        if root is None:
            return -sys.maxint, 0

        left = self.maxPathSumHelper(root.left)
        right = self.maxPathSumHelper(root.right)

        maxpath = max(left[0],right[0], root.val+left[1]+right[1])
        single = max(left[1] + root.val, right[1] + root.val,0)

        return maxpath, single