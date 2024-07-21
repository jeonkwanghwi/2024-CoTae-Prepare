import sys
sys.setrecursionlimit(10 ** 6)


n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

foods = []  # 음쓰들
foodWaste = 0  # 음쓰

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(k):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = 1  # 음식물 표시

def DFS(x, y):
    global foodWaste
    foodWaste += 1
    graph[x][y] = 0 # 현재지점 방문

    # 그래프에 덮어 씌워도 되는 상황이면 visited 안써도 됨.

    # DFS(visited 쓸 수 있음) : 군집화 -> 방문했던 곳을 또 다시 방문하지 않음.
    # BFS(visited 안써도 됨) : 거리, 초단위 가장 짧은 시간, 방문했던 곳을 또 방문할 수도 있음. (그래프는 검증용, 누적 가능)
    # 방문 했던 곳을, 또 방문하지 않기 위해서 visited 쓰는 것임.

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 내고, 음쓰가 있는 곳이라면
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            DFS(nx, ny) # 해당 좌표로 이동


for i in range(n):
    for j in range(m):
        if (graph[i][j] == 1): # 음쓰가 있으면 DFS 실행
            DFS(i, j)
            foods.append(foodWaste) # 음쓰들 모아놓음
            foodWaste = 0  # 음쓰 초기화

print(max(foods))