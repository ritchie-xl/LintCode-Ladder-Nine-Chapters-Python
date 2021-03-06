"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
def maxDepth(self, root):
    # write your code here
    if root is None:
        return 0

    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)

    return max(left, right) + 1
