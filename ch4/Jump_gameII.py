# @param A, a list of integers
# @return an integer
def jump(A):
    # write your code here
    if not A:
        return A

    farthest = 0
    end = 0
    jump = 0

    # for i in range(1,len(A)):
    #     if farthest<= len(A) -1 and i + A[i] >= farthest:
    #         farthest = i + A[i]
    #         ret += 1
    #
    #     if farthest >= len(A)-1:
    #         return ret
    #
    # return ret

    while end < len(A) - 1:
        jump += 1
        for i in range(end+1):
            if A[i] + i > farthest:
                farthest = A[i] + i
        start = end + 1
        end = farthest

    return jump



