n, m = map(int, input().split())
s = []

def backTracking(): # DFS를 이용함
    if len(s) == m: # m개가 모였다면 출력
        print(*s)
        return
    for i in range(1, n+1): # m개의 숫자가 모이는 과정인데, prev를 통해 중복 출력을 방지함.
        s.append(i)  # 1~n까지 값을 넣는 것이기 때문에 굳이 list 초기화 하지 않아도 됨
        backTracking()
        s.pop()


backTracking()