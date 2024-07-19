from collections import deque

n, k = map(int, input().split())
maxSize = 100000
visited = [0] * (maxSize + 1)  # 각 위치를 방문했는지 여부 & 해당 위치까지 도달하는 데 걸린 시간
# 0이 아니니까 방문했다! 이거로 끝나는 게 아니고, 해당 숫자가 거기 인덱스까지 가는데 걸린 시간을 의미.

def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        current = queue.popleft()
        if current == k: # 탈출 조건
            return visited[k] # value가 결국 time값. 즉, 해당 current까지 가는데 걸린 값이 value고, 시간을 의미.
        
        for next in (current+1, current-1, current * 2): # 이동할 수 있는 경우는 이 3가지뿐
            if 0 <= next <= maxSize and visited[next] == 0:
                visited[next] = visited[current] + 1
                queue.append(next)


print(bfs(n)) # visited[k]를 리턴