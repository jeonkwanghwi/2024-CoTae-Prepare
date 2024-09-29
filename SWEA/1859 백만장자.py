T = int(input()) # 테스트 케이스 개수
for t in range(T):
    n = int(input()) # N일동안의 매매가
    prices = list(map(int, input().split()))

    max_price = 0  # 뒤에서부터 본 최대값
    income = 0  # 총 이익

    for i in range(n-1, -1, -1):
        if prices[i] > max_price: # 최대값이면 교체해줌
            max_price = prices[i]
        else: # 최대값 아니면
            income += max_price-prices[i] # 차액이 이익이니깐

    print(f"#{t+1}", income)