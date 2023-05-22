from random import randint

class Solver:
    def __init__(self, s, m = [1000000007, 1000000009]):
        self.s = s
        self.m = m
        self.x = randint(1, 10 ** 9)
        self.h = [[0 for _ in range(len(m))] for _ in range(len(self.s) + 1)]
        for i in range(1, len(self.s) + 1):
            for j in range(len(m)):
                self.h[i][j] = (self.x * self.h[i - 1][j] + ord(self.s[i - 1])) % self.m[j]


    def computeHash(self, start, length):
        hashes = [0] * len(self.m)
        for i in range(len(self.m)):
            y = pow(self.x, length, self.m[i])
            hashes[i] = (self.h[start + length][i] - y * self.h[start][i]) % self.m[i]

        return hashes


    def ask(self, a, b, l):
        hash_a = self.computeHash(a, l)
        hash_b = self.computeHash(b, l)
        return hash_a == hash_b


s = input()
q = int(input())
solver = Solver(s)
for i in range(q):
    a, b, l = map(int, input().split())
    print("Yes" if solver.ask(a, b, l) else "No")
