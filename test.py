# def solution(n, stages):
#     stages.sort()
#     tmp = dict()
#     for i in range(1, n+1):
#         tmp[i] = 0
#     ans = []
#
#     for i in range(1, n+1):
#         if i not in stages:
#             tmp[i] = 0
#             continue
#         tmp[i] = stages.count(i) / (len(stages)-stages.index(i))
#         print(stages.count(i), end=' ')
#         print(len(stages)-stages.index(i))
#
#     print(tmp.keys())
#     return tmp
#
#
# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print()
# print(solution(4, [4,4,4,4,4]))