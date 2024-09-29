T = int(input())

for test_case in range(1, T + 1):
    a, b, n = map(int, input().split())
    cnt = 0
    while True:
        if a > n or b > n:
            break
        if a > b:
            a, b = b, a
        # a가 작은값, b가 큰값
        a += b
        cnt += 1

    print(cnt)
