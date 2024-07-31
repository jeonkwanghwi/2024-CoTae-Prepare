k, n, = map(int, input().split()) # k : 이미 가진 랜선개수 / n : 필요한 랜선개수
lans = []
for i in range(k):
    lans.append(int(input()))

left = 1
right = max(lans)

while left <= right:
    cnt = 0
    mid = (left+right)//2
    for line in lans:
        cnt += line//mid

    # 잘린 개수가 목표치보다 많으면 더 길게 잘라야함
    if cnt >= n:
        left = mid + 1
    else:
        right = mid - 1
print(right)