from collections import deque
def solution(bridge_length, weight, truck_weights):

    truck_weights = deque(truck_weights)  # truck_weights를 deque으로 변환
    onthebridge = deque([0] * bridge_length) # 다리 길이만큼 초기화하기
    time = 0
    current_bridge_weight = 0 # 현재 다리 무게

    while onthebridge: # 모든 트럭이 넘어갈 때까지 진행
        time += 1
        current_bridge_weight -= onthebridge.popleft() # 다리에서 트럭 한 대가 내려감

        if truck_weights: # 올라갈 트럭이 있다면
            if current_bridge_weight + truck_weights[0] <= weight: # 현재 다리 무게 + 올라갈 트럭의 무게
                truck = truck_weights.popleft()
                onthebridge.append(truck)
                current_bridge_weight += truck
            else:
                onthebridge.append(0)

        # 모든 트럭이 다리를 건넜으면 반복을 종료
        if not onthebridge and not truck_weights:
            break

    return time


# 테스트
print("answer = ", solution(2, 10, [7, 4, 5, 6])) # 8
print("answer = ", solution(100, 100, [10])) # 101
print("answer = ", solution(100, 100, [10,10,10,10,10,10,10,10,10,10])) # 110


# 처음 코드 (폐기)
# def solution(bridge_length, weight, truck_weights):
#
#     truck_weights.reverse() # 6 5 4 7
#     onthebridge = [0 for _ in range(bridge_length)]
#
#     onthebridge.pop()
#     onthebridge.insert(0, truck_weights.pop()) # 트럭 하나 올림
#     time = 1
#
#     print("onthebridge = ", onthebridge,"\ntruck_weights = ", truck_weights)
#
#     while sum(onthebridge) != 0: # 다리 위에 트럭이 있을 때 까지만 -> 트럭이 있다면 무게가 있다는 뜻이니 0이 아님
#         if len(truck_weights) > 0: # 건널 트럭이 남아있다면
#             newtruck = truck_weights.pop()
#             onthebridge.pop()
#
#             if weight >= sum(onthebridge) + newtruck: # 올라갈 무게가 된다면 올리기
#                 onthebridge.insert(0, newtruck)  # 트럭 하나 올림
#             else: # 올라갈 무게가 안되면 앞차만 전진
#                 onthebridge.insert(0, 0)
#             time += 1 # 무게 되면 올리고, 안되면 전진이니까 time은 마지막에 1번만 올림
#
#         else: # 건널 트럭 없는 경우
#             onthebridge.pop()
#             onthebridge.insert(0, 0)
#             time += 1
#
#         print("time = ", time , "onthebridge = ", onthebridge)
#
#     return time
#
# print("answer = ", solution(2, 10, [7,4,5,6]))