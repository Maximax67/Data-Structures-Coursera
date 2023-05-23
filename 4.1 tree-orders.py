import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(input())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, input().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []

    def goThrough(root):
      if self.left[root] != -1:
        res = goThrough(self.left[root])
        if res:
          self.result.append(res)
    
      self.result.append(self.key[root])
    
      if self.right[root] != -1:
        res = goThrough(self.right[root])
        if res:
          self.result.append(res)

    goThrough(0)

    return self.result

  def preOrder(self):
    self.result = []
    
    def goThrough(root):
      self.result.append(self.key[root])
      
      if self.left[root] != -1:
        res = goThrough(self.left[root])
        if res:
          self.result.append(res)

      if self.right[root] != -1:
        res = goThrough(self.right[root])
        if res:
          self.result.append(res)

    goThrough(0)

    return self.result

  def postOrder(self):
    self.result = []

    def goThrough(root):
      if self.left[root] != -1:
        res = goThrough(self.left[root])
        if res:
          self.result.append(res)

      if self.right[root] != -1:
        res = goThrough(self.right[root])
        if res:
          self.result.append(res)

      self.result.append(self.key[root])

    goThrough(0)

    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
