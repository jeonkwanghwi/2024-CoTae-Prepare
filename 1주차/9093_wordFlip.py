for _ in range(int(input())):
    lst = input().split()
    for i in range(len(lst)):
        lst[i] = lst[i][::-1] # 각 원소별 순서 뒤집기
        print(lst[i], end=' ')


# from collections import deque
#
# for _ in range(int(input())):
#     lst = deque(list(input().split()))
#         print(i)