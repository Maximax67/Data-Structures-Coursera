class HashTable:
    def __init__(self, s, p_length, x, m):
        self.x = x
        self.m = m
        self.h = [0 for _ in range(len(s) - p_length + 1)]
        substr = s[len(s) - p_length:]
        self.h[len(s) - p_length] = self.computeHash(substr)
        y = pow(x, p_length, m)
        for i in range(len(s) - p_length - 1, - 1, - 1):
            self.h[i] = (x * self.h[i + 1] + ord(s[i]) - y * ord(s[i + p_length])) % m

    def computeHash(self, s):
        h = 0
        for i in range(len(s) - 1, -1, -1):
            h = (h * self.x + ord(s[i])) % self.m
        return h


class HashDictionary:
    def __init__(self, s, p_length, x, m):
        self.x = x
        self.m = m
        self.dictionary = {}
        substr = s[len(s) - p_length:]
        last = self.computeHash(substr)
        self.dictionary[last] = len(s) - p_length
        y = pow(x, p_length, m)
        for i in range(len(s) - p_length - 1, - 1, - 1):
            curr = (x * last + ord(s[i]) - y * ord(s[i + p_length])) % m
            self.dictionary[curr] = i
            last = curr

    def computeHash(self, s):
        h = 0
        for i in range(len(s) - 1, -1, -1):
            h = (h * self.x + ord(s[i])) % self.m

        return h


def searchSubstr(ht, hd):
    check = False
    matches = {}
    for i in range(len(ht.h)):
        b_start = hd.dictionary.get(ht.h[i], -1)
        if not b_start == -1:
            check = True
            matches[i] = b_start
    return check, matches


def calculateMaxLength(a, b, l, h, max_len, a_start, b_start):
    if l > h:
        return a_start, b_start, max_len

    mid = (l + h) // 2
    m1 = 1000000007
    m2 = 1000004249
    x = 100
    ht1 = HashTable(a, mid, x, m1)
    ht2 = HashTable(a, mid, x, m2)
    hd1 = HashDictionary(b, mid, x, m1)
    hd2 = HashDictionary(b, mid, x, m2)
    check1, match1 = searchSubstr(ht1, hd1)
    check2, match2 = searchSubstr(ht2, hd2)
    if check1 and check2:
        for v1, v2 in match1.items():
            if not match2.get(v1, -1) == -1:
                del ht1, ht2, hd1, hd2, match1, match2, check1, check2
                return calculateMaxLength(a, b, mid + 1, h, mid, v1, v2)

    return calculateMaxLength(a, b, l, mid - 1, max_len, a_start, b_start)


while True:
    line = input()
    if line == '':
        break

    s, t = line.split()
    if len(s) <= len(t):
        short_string, long_string = s, t
    else:
        short_string, long_string = t, s

    k = len(short_string)

    l, i, j = calculateMaxLength(long_string, short_string, 0, k, 0, 0, 0)

    if len(s) <= len(t):
        print(i, l, j)
    else:
        print(l, i, j)
