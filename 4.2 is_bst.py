def goInOrder(tree):
  stack = []
  inOrderTree = []
  current = 0
  while current != -1 or stack:
    if current == -1:
      root = stack.pop()
      inOrderTree.append(root[0])
      current = root[2]
    else:
      root = tree[current]
      stack.append(root)
      current = root[1]

  return inOrderTree


def IsBinarySearchTree(tree):
  n = len(tree)
  if n < 2:
    return True

  tree = goInOrder(tree)

  for i in range(1, n):
    if tree[i] <= tree[i - 1]:
      return False

  return True


def main():
  nodes = int(input().strip())
  tree = []
  for _ in range(nodes):
    tree.append(list(map(int, input().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")


if __name__ == "__main__":
  main()
