"""
@param grid: a list of lists of integers.
@return: An integer, minimizes the sum of all numbers along its path
"""
def minPathSum(grid):
    # write your code here
    if not grid:
        return grid

    m = len(grid)
    n = len(grid[0])

    ret = [[grid[0][0]]]

    for i in range(1,n):
        ret[0].append(grid[0][i] + ret[0][i-1])

    for j in range(1,m):
        ret.append([grid[j][0] + ret[j-1][0]])

    for i in range(1,m):
        for j in range(1,n):
            ret[i].append(grid[i][j] + min(ret[i][j-1],ret[i-1][j]))

    return ret[m-1][n-1]

