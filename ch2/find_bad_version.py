# class VersionControl:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use VersionControl.isBadVersion(10) to check whether version 10 is a
# bad version.

"""
@param n: An integers.
@return: An integer which is the first bad version.
"""
class VersionControl:
    def init(self):
        self.list = [False, False,True,True]

    def isBadVersion(self,n):
        return self.list[n-1]


def findFirstBadVersion(self, n):
    # write your code here
    if n is None or n <= 1:
        return n

    start = 0
    end = n
    while start + 1 < end:
        mid = (start + end) / 2

        l1 = VersionControl.isBadVersion(mid)

        if l1 == True:
            end = mid
        else:
            start = mid

    ls = VersionControl.isBadVersion(start)
    le = VersionControl.isBadVersion(end)

    if ls == True:
        return start
    if le == True:
        return end
    return -1
