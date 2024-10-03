t = int(input())
for test_case in range(t):
    lst = sorted(map(int, input().split()))
    # 소수점 첫째 자리에서 반올림한 정수 출력하기
    print(f"#{test_case+1}", round(sum(lst[1:9])/8))