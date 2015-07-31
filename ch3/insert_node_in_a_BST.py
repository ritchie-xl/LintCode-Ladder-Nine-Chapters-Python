__author__ = 'lei'

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode_1(self, root, node):
        # write your code here
        if root is None:
            return node

        temp = root
        last = TreeNode(None)

        while temp is not None:
            last = temp
            if temp.val > node.val:
                temp = temp.left
            else:
                temp = temp.right

        if last is not None:
            if last.val > node.val:
                last.left = node
            else:
                last.right = node

        return root

