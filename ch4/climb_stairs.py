"""
@param n: An integer
@return: An integer
"""
def climbStairs_1(n):
    # write your code here
    if not n or n == 0 or n == 1:
        return n
    return search(n)


def search(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return search(n-1) + search(n-2)

def climbStairs_2(n):
    # write your code here
    if not n or n ==0:
        return

    ret = [1,2]

    for i in range(2,n):
        ret.append(ret[i-1]+ret[i-2])
    return ret[n-1]