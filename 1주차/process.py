from collections import deque

def solution(priorities, location):
    ans = 0
    priorities = deque(priorities)

    while priorities:  # 안에 있는 값이 다 사라질 때 까지
        if priorities[0] >= max(priorities): # 맨 앞이 최대면 pop
            priorities.popleft()
            ans += 1
            if location == 0:
                break
        else: # 맨 앞이 최대가 아닌 일반적인 경우
            priorities.append(priorities.popleft())

        """ pop 할 때에도 location 값을 줄여줘야하므로 공통되는 부분은 if-else 밖으로 뺌. (처음에 이거 안해서 틀림) """
        location -= 1

        if location < 0: # 음수일 때 location 값 보정
            location = len(priorities) - 1

    return ans

print(solution([2, 1, 3, 2], 2)) # 답 1
print(solution([1, 1, 9, 1, 1, 1], 0)) # 답 5