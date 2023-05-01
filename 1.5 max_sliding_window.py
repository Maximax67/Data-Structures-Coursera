from collections import deque


def max_sliding_window(sequence, m):
    queue = deque()
    max_val = []

    for i in range(len(sequence)):
        while queue and sequence[i] >= sequence[queue[-1]]:
            queue.pop()
        queue.append(i)
        if queue and i >= m and queue[0] == i - m:
            queue.popleft()
        if i >= m - 1:
            max_val.append(sequence[queue[0]])

    return max_val


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))

