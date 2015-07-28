def anagram(self, s, t):
    # write your code here
    if s is None and t is None:
        return True

    if s is None or t is None:
        return False

    if len(s) != len(t):
        return False

    tmp1 = dict()
    tmp2 = dict()

    for i in range(len(s)):
        if s[i] in tmp1:
            tmp1[s[i]] = tmp1[s[i]] + 1
        else:
            tmp1[s[i]] = 1

        if t[i] in tmp2:
            tmp2[t[i]] = tmp2[t[i]] + 1
        else:
            tmp2[t[i]] = 1

    return tmp1 == tmp2

