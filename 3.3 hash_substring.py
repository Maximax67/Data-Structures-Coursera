from random import randint

def polyhash(S, p, x):
    h = 0
    for i in range(len(S) - 1, -1, -1):
        h = (h * x + ord(S[i])) % p
    
    return h


def precomputedHashes(T, P, p, x):
    H = [None for _ in range(len(T) - P + 1)]
    S = T[len(T) - P : ]
    H[len(T) - P] = polyhash(S, p, x)
    y = 1
    
    for _ in range(1, P + 1):
        y = (y * x) % p
    
    for i in range(len(T) - P - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + P])) % p
    
    return H


def rabinKarp(P, T):
    p = 1000000007
    x = randint(1, p - 1)
    positions = []
    pHash = polyhash(P, p, x)
    H = precomputedHashes(T, len(P), p, x)
    
    for i in range(len(T) - len(P) + 1):
        if pHash == H[i]:
            positions.append(i)
    
    return positions


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


if __name__ == '__main__':
    print_occurrences(rabinKarp(*read_input()))
