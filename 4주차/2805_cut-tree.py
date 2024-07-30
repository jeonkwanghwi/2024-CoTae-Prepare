n, m = map(int, input().split())

# 나무들 자체에 대해서 높이를 구하는 게 아니고 절단기의 높이를 구하는 거라서 이분탐색을 쓰더라도 정렬을 여기서 할 필요는 없음.
trees = list(map(int, input().split()))

# 절단기의 높이를 이분탐색으로 찾기
# 절단기 높이는 짧을수록 나무를 더 많이 자르는 것임. (중요)

left = 0 # 나무 높이 최소가 0이라서 0으로 설정
right = trees[-1]

while left <= right:
    mid = (left + right) // 2
    sum = 0

    # 각 반복마다 mid값(절단기 높이)을 설정하고, 해당 절단기로 나무들 잘라봄. 잘린 나무들 합이 sum
    for tree in trees:
        if tree-mid > 0:
            sum += (tree - mid)

    # mid로 잘랐을 때 나무 합이 m보다 크면 나무 합이 m보다 크다면 더 적게 잘라야함
    if sum >= m: # 절단기의 "최대높이"를 알아야하므로 sum이 m과 같은 시점이 되어도(탈출조건), 더 진행해서 절단기 높이를 최대한 높여야함!!! (중요)
        left = mid + 1 # 절단기 높이를 더 올림 (더 적은 나무를 자르게 됨)

    # mid로 잘랐는데 나무가 부족하면 더 잘라야하니까 right를 내려서 더 잘라야함
    else:
        right = mid - 1 # 절단기 높이를 더 내림 (더 많은 나무를 자르게 됨)

# right를 출력하는 이유는 left가 right보다 커지는 시점에서 right는 가장 마지막으로 가능한 높이를 의미하기 때문임
print(right)