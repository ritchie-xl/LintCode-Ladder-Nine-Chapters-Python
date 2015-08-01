import copy

"""
@param root: The root of the binary search tree.
@param A and B: two nodes in a Binary.
@return: Return the least common ancestor(LCA) of the two nodes.
"""
def lowestCommonAncestor(self, root, A, B):
    # write your code here

    if not root or root == B or root == A:
        return root

    left = self.lowestCommonAncestor(root.left, A , B)
    right = self.lowestCommonAncestor(root.right, A , B)

    if left and right:
        return root
    elif left:
        return left
    elif right:
        return right
    else:
        return None



