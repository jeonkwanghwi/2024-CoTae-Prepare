def solution(prices):
    lst = []
    for i in range(len(prices)):
        time = 0
        for j in range(i+1, len(prices)):
            time += 1
            if prices[i] > prices[j]:
                break
        lst.append(time)
    return lst

print(solution([1, 2, 3, 2, 3]))


