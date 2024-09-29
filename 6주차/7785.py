import sys
input = sys.stdin.readline

lst = []
for i in range(int(input())):
    p, q = input().split()
    if p not in lst:
        lst.append(p)
    else:
        lst.remove(p)

for i in lst:
    print(i)