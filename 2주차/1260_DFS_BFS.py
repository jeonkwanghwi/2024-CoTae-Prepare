from collections import deque

n, m, v = map(int, input().split()) # 정점, 간선, 탐색 시작할 정점의 번호
graph = [[False] * (n + 1) for _ in range(n + 1)] # 그래프 선언

# 주어진 정보로 정점간 연결하기 (문제에 주어진 그래프 초기화 하기)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True # a->b가 연결되어있다.
    graph[b][a] = True # b->a가 연결되어있다.

# visited를 선언할 때 n+1개 선언하는 이유는 노드 넘버링이 1부터 시작하기 때문
visited1 = [False] * (n + 1)  # dfs 방문기록
visited2 = [False] * (n + 1)  # BFS 방문기록
############################################## 초기세팅 끝

def DFS(v):
    visited1[v] = True # 현재 노드는 방문한것
    print(v, end=' ') # 방문한 노드 출력
    for i in range(1, n+1):
        if visited1[i] == False and graph[v][i] == 1: # 해당 노드를 아직 방문하지 않았고, 노드 i와 연결되어 있는 경우
            DFS(i) # 방문하지 않은 노드 계속 방문

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