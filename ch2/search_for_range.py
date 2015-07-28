def searchRange(A, target):
    # write your code here
    if A is None or target is None or len(A) == 0:
        return [-1, -1]

    start, end = 0, len(A)-1

    while start + 1 < end:
        mid = (start + end) / 2
        if A[mid] < target:
            start = mid
        else:
            end = mid

    if A[start] == target:
        left = start
    elif A[end] == target:
        left = end
    else:
        return [-1, -1]

    start, end = left, len(A)-1

    while start + 1 < end:
        mid = (start + end) / 2
        if A[mid] <= target:
            start = mid
        else:
            end = mid

    if A[end] == target:
        right = end
    else:
        right = start

    return [left, right]
