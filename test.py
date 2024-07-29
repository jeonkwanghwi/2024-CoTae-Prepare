n, s = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0 # 부분 수열의 개수
lst = []
def backTracking(idx):
    global cnt
    if sum(lst) == s and len(lst) > 0: # 빈 리스트 []이것도 sum을 해보면 0으로 찍혀서, 빈 리스트를 제외하기 위해서 len(lst)는 0보다 커야함.
        cnt += 1
    for i in range(idx, n):
        lst.append(nums[i]) # 1 2 3 4
        backTracking(i+1) # 이전 원소 중복해서 체크하지 않기 위해
        lst.pop()


backTracking(0)
print(cnt)
