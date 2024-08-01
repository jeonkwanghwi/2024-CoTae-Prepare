n = int(input())
boj = input()

# 여기서 dp[i]의 값은 해당 인덱스까지 가는데에 드는 에너지를 의미함.
# 문제 조건에서 적힌 N의 최대값이 1000이라서, 첫번째에서 마지막으로 바로 점프하더라도 1000000을 넘지 않음
dp = [1000000]*n
dp[0] = 0

for i in range(n):
    for j in range(i+1, n):
        if (boj[i]=="B" and boj[j]=="O") or (boj[i]=="O" and boj[j]=="J") or (boj[i]=="J" and boj[j]=="B"):
            dp[j] = min(dp[j], dp[i] + (j-i)**2 ) # j-i는 인덱스끼리 떨어진 거리를 의미

        # if문을 3개 써도 dp 비교하는 구문이 동일해서 or로 합침
        # if 3개와, or로 묶은 것은 or이 근소하게 빨랐는데, 큰 의미는 없을듯 (-36ms)

# for문이 끝났는데도 마지막 값이 안바뀌었으면 스타트가 링크를 만나지 못한 것임
if dp[-1] == 1000000:
    print(-1)
else:
    print(dp[-1])