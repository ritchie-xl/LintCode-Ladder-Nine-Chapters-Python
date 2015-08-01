"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
"""
def searchRange(root, k1, k2):
    # write your code here
    if not root: return []

    global result
    result = []
    search(root,k1,k2)

    return  result

def search(root, k1, k2):
    if not root: return


    if k1 < root.val:
        search(root.left, k1, k2)

    if k1 <= root.val <= k2:
        result.append(root.val)

    if k2 > root.val:
        search(root.right, k1, k2)

