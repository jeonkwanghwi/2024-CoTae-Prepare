def solution(n, times):
    # left = 최소시간 , right = 최대시간

    left = 1  # 최소시간은 1분이상이라고 문제에 명시
    right = max(times) * n  # 모든 사람이 가장 느린 심사관에게 심사를 받을 때가 최대시간

    while left < right:
        mid = (left + right) // 2
        # total = 각 심사관이 mid 시간 동안 심사할 수 있는 사람의 수를 계산
        total = sum(mid // time for time in times)

        # total이 n 이상이면 가능한 시간을 "줄이기" 위해 right = mid
        if total >= n:
            right = mid
        # total이 n 미만이면 가능한 시간을 "늘리기" 위해 left = mid + 1
        else:
            left = mid + 1
    # 최종적으로 left가 최소시간을 가리키게 됨.
    return left