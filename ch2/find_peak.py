def findPeak(A):
    # write your code here
    if len(A) <=1 or A is None:
        return A

    start = 0
    end = len(A)-2

    while start + 1 < end:
        mid = (start + end ) /2
        if A[mid] < A[mid + 1]:
            start = mid
        else:
            end = mid

    if A[start] < A[end]:
        return end
    else:
        return start




