import sys
from itertools import combinations
input = sys.stdin.readline

answer = []

# 가능한 모든 게임 조합 - 총 15개 게임 (0,1), (0,2), ... , (4,5)
game = list(combinations(range(6), 2))


def backTracking(round):
    global ans
    if round == 15: # 모든 게임을 다 처리한 경우
        ans = 1
        # 각 국가의 승/무/패 결과가 모두 소진된 경우만 유효함
        for sub in result:
            if sub.count(0) != 3:  # 승, 무, 패가 모두 0이어야 함
                ans = 0
                break
        return

    # 현재 게임에서의 두 팀
    t1, t2 = game[round]

    # 가능한 경기 결과 (승/패, 무/무, 패/승)
    for x, y in ((0, 2), (1, 1), (2, 0)):
        # t1이 x 결과를, t2가 y 결과를 가질 수 있는지 확인
        if result[t1][x] > 0 and result[t2][y] > 0:
            # 경기 결과 반영
            result[t1][x] -= 1
            result[t2][y] -= 1

            # 다음 게임으로 넘어감
            backTracking(round + 1)

            # 백트래킹: 원래 상태로 되돌림
            result[t1][x] += 1
            result[t2][y] += 1

# 4번의 결과에 대해 처리
for _ in range(4):
    data = list(map(int, input().split()))
    result = [data[i:i + 3] for i in range(0, 18, 3)]
    ans = 0
    backTracking(0)
    answer.append(ans)

print(*answer)
