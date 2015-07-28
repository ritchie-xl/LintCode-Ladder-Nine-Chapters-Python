__author__ = 'ritchie'
def strStr_1(source, target):
        # write your code here
        if source is None or target is None: return -1

        l1 , l2= len(source) , len(target)

        if l2 > l1: return -1
        if l2 == 0: return 0

        for i in range(l1):
            for j in range(l2):
                if target[j] != source[i+j]:
                    break
                if j+1 == l2 and target[j] == source[i+j]:
                    return i
                if i + j + 1 == l1:
                    return -1

        return -1

def strStr_2(source, target):
    if source is None or target is None:
        return -1

    l1, l2 = len(source), len(target)
    if l2 > l1: return -1
    if l2 == 0: return 0

    for i in range(l1-l2+1):
        for j in range(l2):
            if source[i+j] != target[j]:
                break
        if j+1 == l2:
            return i
    return -1

def strStr_3(source, target):
    if source is None or target is None:
        return -1

    l1, l2 = len(source), len(target)
    if l2 > l1: return -1
    if l2 == 0: return 0

    for i in range(l1-l2+1):
        for j in range(l2):
            if source[i+j] != target[j]:
                break
        if j+1 == l2:
            return True

    return False