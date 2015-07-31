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

        return self.help(root, A, B)


    def help(self,root, A, B):
        if not (A and B) or root is None:
            return root

        if A <= root.val <= B or B <= root.val <= A:
            return root

        if min(A,B) > root.val:
            return self.help(root.right, A, B)

        if max(A,B) < root.val:
            return self.help(root.left, A, B)



