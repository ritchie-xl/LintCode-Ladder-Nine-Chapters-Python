
"""
@param n and m: positive integer(1 <= n , m <= 100)
@return an integer
"""
def uniquePaths( m, n):
    # write your code here
    if not m or not n:
        return

    # Initialization
    ret = [[1]*n]

    for i in range(1,m):
        ret.append([1])
        for j in range(1,n):
            ret[i].append(ret[i][j-1]+ret[i-1][j])

    return ret[m-1][n-1]
