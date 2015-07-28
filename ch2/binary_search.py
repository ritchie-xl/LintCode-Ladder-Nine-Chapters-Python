def binarySearch(nums, target):
    # write your code here
    if target is None or nums is None \
            or len(nums) == 0:
        return -1

    start = 0
    end = len(nums)

    while start + 1 < end:
        mid = (start + end) / 2
        if nums[mid] > target:
            end = mid
        elif nums[mid] < target:
            start = mid
        else:
            end = mid

    if nums[start] == target:
        return start

    if nums[end] == target:
        return end

    return -1
