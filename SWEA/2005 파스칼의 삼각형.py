T = int(input())

for test_case in range(1, T + 1):
    print(f"#{test_case}")
    n = int(input())  # n은 1~10

    pascal = []
    for i in range(1, n+1):
        pascal.append([1]*i)

    if n > 2:
        for i in range(2, n):
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    # 출력하기 (1)
    for i in range(n):
        for j in range(i+1):
            print(pascal[i][j], end=' ')
        print()

    # 또 다른 출력방법 (2)
    # for i in pascal:
    #     print(*i)