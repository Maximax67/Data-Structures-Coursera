from collections import deque

class HashTable:
    def __init__(self, s, m, x):
        self.m = m
        self.x = x
        self.h = [0 for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            self.h[i] = (self.h[i - 1] * self.x + ord(s[i - 1])) % self.m
    
    def getHashValue(self, start, length):
        y = pow(self.x, length, self.m)
        return (self.h[start + length] - y * self.h[start]) % self.m


def isMatch(ht1, ht2, a_start, length, p_length, k):
    stack = deque()
    stack.append((a_start, 0, length, 1))
    stack.append((a_start + length, length, p_length - length, 1))
    C = 0
    t = 2
    counter = 0
    while stack:
        a, b, L, n = stack.popleft()
        e1 = ht1.getHashValue(a, L)
        e2 = ht2.getHashValue(b, L)
        if t != n:
            counter = C
        if e1 != e2:
            counter += 1
            if L > 1:
                stack.append((a, b, L // 2, n + 1))
                stack.append((a + L // 2, b + L // 2, L - L // 2, n + 1))
            else:
                C += 1

        if counter > k:
            return False

        t = n

    return counter <= k


def solve(k, t, p):
    x = 100
    m = 1000000007
    ht1 = HashTable(t, m, x)
    ht2 = HashTable(p, m, x)
    positions = []
    for i in range(len(t) - len(p) + 1):
        if isMatch(ht1, ht2, i, len(p) // 2, len(p), k):
            positions.append(i)

    return positions


while True:
    line = input()
    if line == '':
        break

    k, t, p = line.split()
    ans = solve(int(k), t, p)
    print(len(ans), *ans)
