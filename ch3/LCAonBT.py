from node import TreeNode

"""
@param root: The root of the binary search tree.
@param A and B: two nodes in a Binary.
@return: Return the least common ancestor(LCA) of the two nodes.
"""
def lowestCommonAncestor(root, A, B):
    # write your code here
    if root is None or root == A or root == B:
        return root

    left = lowestCommonAncestor(root.left, A , B)
    right = lowestCommonAncestor(root.right, A ,B)

    if left and right:
        return root
    elif left:
        return left
    elif right:
        return right
    else:
        return None








