__author__ = 'lei'

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        if root is None:
            return True

        return self.dfs(root,float('-inf'),float('inf'))

    def dfs(self,root,low,up):
        if root is None:
            return True

        if root.val >= up or root.val <= low:
            return False

        return self.dfs(root.left, low, root.left.val) \
                and self.dfs(root.right, root.right.val,up)
