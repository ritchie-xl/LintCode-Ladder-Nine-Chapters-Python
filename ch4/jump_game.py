# Version I: DP
def canJump(A):
    if not A:
        return True

    n = len(A)
    ret = [False]*n
    ret[0] = True

    for i in range(1, n):
        for j in range(i):
            if ret[j] and j + A[j] >= i:
                ret[i] = True
                break

    return ret[n-1]

#Version II: Greedy
def canJump(A):
    if not A:
        return True

    farthest = A[0]

    for i in range(1,len(A)):
        if i < farthest and i+A[i] > farthest:
            farthest = i+A[i]

    return farthest >= len(A)-1