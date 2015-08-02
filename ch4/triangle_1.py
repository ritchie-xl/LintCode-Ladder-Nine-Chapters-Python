
"""
@param triangle: a list of lists of integers.
@return: An integer, minimum path sum.
"""
def minimumTotal(triangle):
    # write your code here
    if not triangle:
        return triangle

    ret = triangle[-1]

    for i in range(2, len(triangle)+1):
        for j in range(len(triangle[-i])):
            ret[j] = triangle[-i][j] + min(ret[j],ret[j+1])

    return ret[0]