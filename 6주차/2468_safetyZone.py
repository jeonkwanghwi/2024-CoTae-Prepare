import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = []
area = []
cnt = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

# n보다 큰 곳만 dfs 탐색, dfs 탐색 구역을 출력
def dfs(x, y):
    global cnt
    graph[x][y] = 0 # 방문처리 (높이가 1이상이니까 0을 방문이라고 처리함)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n and 0 <= ny < n) and graph[nx][ny] > n:
            cnt += 1
            dfs(nx, ny)


for i in range(1, n):
    for j in range(n):
        if graph[i][j] > n:
            dfs(i, j)
            area.append(cnt)
            cnt = 0

print(graph)
print(len(area))
