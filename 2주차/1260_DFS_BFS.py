from collections import deque

n, m, v = map(int, input().split()) # 정점, 간선, 탐색 시작할 정점의 번호
graph = [[False] * (n + 1) for _ in range(n + 1)] # 그래프 선언

dx = [0, 0, 1, -1] # x축 방향 이동
dy = [1, -1, 0, 0] # y축 방향 이동

# 주어진 정보로 정점간 연결하기 (문제에 주어진 그래프 초기화 하기)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True # a->b가 연결되어있다.
    graph[b][a] = True # b->a가 연결되어있다.

# visited를 선언할 때 n+1개 선언하는 이유는 노드 넘버링이 1부터 시작하기 때문
visited1 = [False] * (n + 1)  # dfs 방문기록
visited2 = [False] * (n + 1)  # BFS 방문기록
############################################## 초기세팅 끝

def DFS(graph, x, y):
    # 오류가 나는 상황을 정리한 것. 위, 아래로 움직이다가 x, y의 범위 밖으로 나가는 경우를 의미함.
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1: # 1인 집은 탐색 대상임
        global part_house # 구역별 집 개수를 의미함
        part_house += 1
        graph[x][y] = 0 # 탐색 후, 탐색 완료의 의미로 0으로 바꿈
        for i in range(4): # 상하좌우 4개의 방향을 체크함
            nx = x + dx[i] # 기존의 좌표에 상하좌우를 더해줌
            ny = y + dy[i]
            DFS(graph, nx, ny) # 더해준 상하좌우로 다시 탐색
        return True # 모든 탐색이 완료됨
    return False # 탐색이 끝나긴 했는데 0을 만나서 끝남. 즉 1로 둘러싼 경계 밖을 간 것.

def BFS(v):
    queue = deque([v])
    visited2[v] = True # 현재 노드는 방문한것

    while queue:
        v = queue.popleft()
        print(v, end=' ') # 방문한 노드 출력
        for i in range(1, n+1):
            if visited2[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited2[i] = 1 # 방문처리
    return queue

DFS(v)
print()
BFS(v)