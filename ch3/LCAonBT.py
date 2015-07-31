"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """ 
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root is None:
            return None

        return self.find(root, A, B)

    def find(self,root, A, B):

        r1 = self.findHelper(root.right,A)
        r2 = self.findHelper(root.right,B)
        l1 = self.findHelper(root.left,A)
        l2 = self.findHelper(root.left,B)

        if (r1 and l2) \
                or (r2 and l1):
            return root
        elif r1 and r2:
            return self.find(root.right, A, B)
        elif l1 and l2:
            return self.find(root.left,A,B)



    def findHelper(self,root, A):
        if not A or root is None:
            return True

        if root.val == A:
            return True
        else:
            left = self.findHelper(root.left, A)
            right = self.findHelper(root.right, A)
            return left and right









