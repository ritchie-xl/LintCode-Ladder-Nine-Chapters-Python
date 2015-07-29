"""
   @param A: sorted integer array A which has m elements,
              but size of A is m+n
   @param B: sorted integer array B which has n elements
   @return: void
"""

def mergeSortedArray(self, A, m, B, n):
    # write your code here
    if B is None or len(B) == 0:
        return A

    i = 0
    b_pos = 0
    while i < m:
        if A[i] < B[b_pos]:
            tmp = A[i + 1:i + 1 + m - b_pos]
            A[i + 1] = B[b_pos]
            A[i + 2:] = tmp
            b_pos = b_pos + 1
        i = i + 1

    return A
