"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
@param root: The root of binary tree.
@return: True if this Binary tree is Balanced, or false.
"""
def isBalanced(self, root):
    # write your code here
    if root is None:
        return True

    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)

    if -2<left-right<2:
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    else:
        return False

    return True

def maxDepth(self, root):
    if root is None:
        return 0

    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)

    return max(left, right)+1
