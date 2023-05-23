import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    stack = [(float('-inf'), tree[0], float('inf'))]
    while stack:
        min_value, root, max_value = stack.pop()
        if root[0] < min_value or root[0] >= max_value:
            return False

        if root[1] != -1:
            stack.append((min_value, tree[root[1]], root[0]))
        if root[2] != -1:
            stack.append((root[0], tree[root[2]], max_value))

    return True


def main():
    n_nodes = int(input())
    nodes = [0 for _ in range(n_nodes)]

    for i in range(n_nodes):
        nodes[i] = [int(x) for x in input().split()]

    if n_nodes == 0 or IsBinarySearchTree(nodes):
        print('CORRECT')
    else:
        print('INCORRECT')


threading.Thread(target=main).start()
