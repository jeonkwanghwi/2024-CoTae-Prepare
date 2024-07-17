import sys
imput = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int, input().split()) # 정점개수 n , 간선개수 m
graph = [[False] * (n + 1) for _ in range(n + 1)] # 그래프 선언
visited = [False] * (n + 1)
count = 0 # 연결 요소 개수

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

def DFS(v):
    visited[v] = True
    for i in range(1, n+1):
        if visited[i] == False:
            DFS(i)

for i in range(1, n+1):
    if visited[i] == False:
        DFS(i)
        count += 1

print(count)