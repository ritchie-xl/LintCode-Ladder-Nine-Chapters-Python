"""
@param n and m: positive integer(1 <= n , m <= 100)
@return an integer
"""
def uniquePathsWithObstacles(obstacleGrid):
    # write your code here
    if not obstacleGrid:
        return

    # Initialization
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    ret = obstacleGrid[:]

    ret[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
    for i in range(1,n):
        ret[0][i] = ret[0][i-1] if obstacleGrid[0][i] ==0 else 0

    for j in range(1,m):
        ret[j][0] = ret[j-1][0] if obstacleGrid[j][0] == 0 else 0

    for i in range(1,m):
        for j in range(1,n):
            if obstacleGrid[i][j] == 1:
                ret[i][j] = 0
            else:
                ret[i][j] = ret[i][j-1] + ret[i-1][j]

    return ret[m-1][n-1]
