"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

def preorderTraversal(self, root):
    # write your code here
    if root is None:
        return []

    stack = [root]
    pre_order = []

    while stack:
        node = stack.pop()
        pre_order.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return pre_order


