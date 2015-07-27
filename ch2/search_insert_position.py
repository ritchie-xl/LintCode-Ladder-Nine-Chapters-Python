__author__ = 'ritchie'
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if len(A) == 0:
            return 0

        start, end = 0, len(A) -1
        if start + 1 < end:
            mid = (start + end)/2
            if A[mid] > target:
                end = mid
            else:
                start = mid

        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return len(A)


s = Solution()
A = [1,3,5,6]
print s.searchInsert(A,4)