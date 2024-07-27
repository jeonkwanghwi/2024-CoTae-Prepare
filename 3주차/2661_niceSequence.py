n = int(input())
nums = []

def check(idx):
    for i in range(1, (idx // 2) + 1):
        if nums[-i:] == nums[-2 * i:-i]: # 리스트 s의 마지막 i개 요소와, 그 앞의 i개 요소가 같다면 중복된 부분 수열이 있다는 뜻
            return False
    return True

def back_tracking(idx):
    if idx == n: # 탈출 조건: 수열의 길이가 n에 도달하면 출력하고 종료
        print(*nums, sep='') # 붙여서 출력하려면 sep 써주면 됨
        exit() # 찾았으니 바로 종료

    for i in range(1, 4): # 1, 2, 3에 대해서만 진행
        nums.append(i)
        if check(idx + 1): # 중복 검사를 통과하면 다음 단계로 진행
            back_tracking(idx + 1)
        nums.pop()

back_tracking(0)
