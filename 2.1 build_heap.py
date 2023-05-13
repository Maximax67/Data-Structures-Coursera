def build_heap(data):
    """
    Build a heap from ``data`` inplace.
    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []
    
    def siftDown(A, i):
        min_index = i
        left = 2 * i + 1
        if left < len(A) and A[left] < A[min_index]:
            min_index = left
        right = 2 * i + 2
        if right < len(A) and A[right] < A[min_index]:
            min_index = right
        if min_index != i:
            A[i], A[min_index] = A[min_index], A[i]
            swaps.append((i, min_index))
            siftDown(A, min_index)
    
    for i in range(len(data) // 2 - 1, -1, -1):
        siftDown(data, i)
    
    return swaps


def main():
    n = int(input())
    data = [int(x) for x in input().split()]
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
