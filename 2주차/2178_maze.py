import sys
from collections import deque
input = sys.stdin.readline

n, m, = map(int, input().split())
maze = [[0] * m for _ in range(n)]
for i in range(n): # 미로 초기화
    tmp = input().rstrip()
    for j in range(m):
        maze[i][j] = int(tmp[j])

dx = [0,0,-1,1]
dy = [1,-1,0,0]

# 이동거리가 1로 고정되지 않은 경우, 다익스트라를 써야함!!!!
def BFS(x, y):
    queue = deque() # 덱 선언
    queue.append((x,y)) # 초기값 append
    while queue:
        x, y = queue.popleft() # 현재 위치 꺼내줌
        for i in range(4): # 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에서 이동하는 상황 & maze 벽이 아닌 경우(값이 0이 아닌 경우)
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1 # 마치 시간을 누적해가듯, 지나간 경로 횟수를 현재 위치에 누적
                queue.append((nx, ny)) # 새로운 nx, ny를 append해줌
    return maze[n-1][m-1] # 도착 위치는 (N-1, M-1)로 고정이므로 이 값을 return


print(BFS(0,0)) # 0,0에서 출발