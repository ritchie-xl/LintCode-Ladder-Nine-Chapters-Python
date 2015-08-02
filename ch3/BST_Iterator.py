"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = Solution(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""
from node import TreeNode
class Solution:
    #@param root: The root of binary tree.

    def __init__(self, root):
        # write your code here
        self.tree = list()
        self.inOrderTraverse(root)
        self.index = -1
        self.size = len(self.tree)


    #@return: True if there has next node, or false
    def hasNext(self):
        # write your code here
        self.index += 1
        return self.index < self.size

    #@return: return next node
    def next(self):
        #write your code here
        return self.tree[self.index]

    def inOrderTraverse(self,root):
        if not root:
            return

        self.inOrderTraverse(root.left)
        self.tree.append(root)
        self.inOrderTraverse(root.right)