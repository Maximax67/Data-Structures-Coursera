from collections import deque


class Stack():
    def __init__(self):
        self.stack = deque()
        self.max = deque()

    def push(self, value):
        if not self.max or value >= self.max[-1]:
            self.max.append(value)
        self.stack.append(value)

    def pop(self):
        if self.stack[-1] == self.max[-1]:
            self.max.pop()
        self.stack.pop()

    def findMax(self):
        return self.max[-1]


if __name__ == '__main__':
    stack = Stack()
    max_val = 0

    num_queries = int(input())
    for _ in range(num_queries):
        query = input().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.findMax())
        else:
            assert(0)
