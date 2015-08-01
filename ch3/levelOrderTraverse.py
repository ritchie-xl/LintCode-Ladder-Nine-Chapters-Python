def levelOrder(root):
    # write your code here
    if not root:
        return root

    a = list()
    a.append(root)

    ret = list()
    while a:
        size = len(a)
        level = list()
        for i in range(size):
            current = a.pop(0)
            if current.left:
                a.append(current.left)

            if current.right:
                a.append(current.right)

            level.append(current.val)

        ret.append(level)

    return ret


