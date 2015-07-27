def binarySearch(nums,target):
    if nums == None or len(nums) == 0:
        return -1

    start = 0
    end = len(nums) - 1

    # Avoid dead while using start + 1 < end
    while start+ 1 < end:
        mid = start + (end-start) /2
        temp = nums[mid]    # Return here is looking for any position
        if temp > target:
            end = mid
        elif temp < target:
            start = mid
        else:
            end = mid

    '''
    Switch these two if looking for last position
    '''
    if (nums[start] == target):
        return start
    if(nums[end] == target):
        return end
    return -1


a = [1,2,3,3,4,5,10]
b = 3

print binarySearch(a,b)