N, S = map(int, input().split())
arr = list(map(int, input().split()))
tmp = []
cnt = 0

def backTracking(start):
    global cnt
    if sum(tmp) == S and len(tmp) > 0:
        cnt += 1

    for i in range(start, len(arr)):
        tmp.append(arr[i])
        backTracking(i + 1)
        tmp.pop()  # 다음 단계로 넘어갈떄

backTracking(0)
print(cnt)