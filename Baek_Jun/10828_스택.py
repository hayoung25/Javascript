import sys


n = int(sys.stdin.readline())
stack = []

for i in range(n):
    input = sys.stdin.readline().split()
    order = input[0]

    if order == 'push':
        stack.append(int(input[1]))
    elif order == 'top':
        if len(stack) > 0: print(stack[-1])
        else: print(-1)
    elif order == 'pop':
        if len(stack) > 0: print(stack.pop())
        else: print(-1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if len(stack) > 0: print(0)
        else: print(1)