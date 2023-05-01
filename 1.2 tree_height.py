import sys
import threading


def tree_recursive(root, nodes):
    height = 1
    max_down = 0
    
    for child in nodes[root][1]:
        current = tree_recursive(child[0], nodes)
        if current > max_down:
            max_down = current
    
    return max_down + height


def compute_height(n, parents):
    nodes = []
    for i in range(n):
        nodes.append([i,[]])
    root = 0
    
    for child_index in range(n):
        parent_index = parents[child_index]
        if parent_index == -1:
            root = child_index
        else:
            nodes[parent_index][1].append(nodes[child_index])
    
    return tree_recursive(root, nodes)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
