def search(self, A, target):
    # write your code here
    if A is None or target is None or len(A) == 0:
        return -1

    start,end = 0, len(A) -1

    while start + 1 < end:
        mid = (start + end) / 2
        if A[mid] == target:
            return mid

        if A[start] < A[mid]:
            if target >= A[start] and A[mid] >= target:
                end = mid
            else:
                start = mid
        else:
            if A[mid] <= target and target <= A[end]:
                start = mid
            else:
                end = mid

    if A[start] == target:
        return start

    if A[end] == target:
        return end

    return -1
