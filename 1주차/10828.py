"""
1. 처음에는 시간초과 났는데, sys.stdin.readline 으로 입력받으니까 바로 해결
2. 한줄에 몇개를 입력받는지 모르는 상황에선 a, b = input().split()처럼 하지 말고 a = input().split()으로 한다.
"""

import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    inst = input().split()

    if inst[0] == "push":
        stack.append(inst[-1])

    elif inst[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif inst[0] == "size":
        print(len(stack))

    elif inst[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif inst[0] == "top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])