def decinal(num):
    stack = []
    while num > 0:
        stack.append(num % 2)
        num = num // 2

    while stack:
        print(stack.pop(), end='')

decinal(10)
