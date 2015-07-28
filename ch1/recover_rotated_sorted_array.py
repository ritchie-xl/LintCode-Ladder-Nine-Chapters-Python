__author__ = 'ritchie'
class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return nums

        for i in range(len(nums)):
            if nums[i] > nums[i] + 1:
                reversed