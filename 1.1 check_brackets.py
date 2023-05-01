def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []
    for i, c in enumerate(text):
        if c in "([{":
            stack.append([c, i])
        elif c in ")]}":
            if stack and are_matching(stack[-1][0], c):
                stack.pop()
            else:
                return i + 1
    
    if stack:
        return stack[-1][1] + 1
    
    return 'Success'


if __name__ == "__main__":
    text = input()
    print(find_mismatch(text))
