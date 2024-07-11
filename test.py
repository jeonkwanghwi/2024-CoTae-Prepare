from collections import deque

example = [1, 2, 3, 4, 5]
dq = deque(example)
dq.rotate(-2)  # 2라고 쓰면 양수이므로 시계방향으로 2번 회전한다.
print(dq)