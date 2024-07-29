import sys
input = sys.stdin.readline
L, C = map(int, input().split())
chars = sorted(input().split()) # 처음부터 오름차순으로 정렬함 (조건 1개를 바로 만족하게 만듦)
vowels = set('aeiou') # 모음 집합

# 모음은 1개만 있어도 됨.
# 자음은 2개 이상
def is_valid(pwd): # 자음, 모음 체크 함수
    if any(alpha in vowels for alpha in pwd) and len(set(pwd)-set(vowels)) >= 2:
        return True
    return False

def backTracking(start, pwd):
    if len(pwd) == L and is_valid(pwd): # 길이가 L이 되고, 유효한 비밀번호 후보라면
        print(''.join(pwd))
        return
    # start부터 C까지 반복해서 다음 문자를 선택
    for i in range(start, C):
        backTracking(i + 1, pwd + [chars[i]]) # 다음 문자를 선택하여 password에 추가하고 재귀 호출


# 0번 인덱스부터 시작, 처음에는 빈 password
backTracking(0, [])



# 처음 시도했다가 틀린 풀이 (시간초과)
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(5000)
#
#
# # L : 암호 후보의 길이
# l, c = map(int, input().split())
# lst = sorted(list(input().split()))
# tmp = []
# visited = [0] * c
# ans = []
#
# # 오름차순 체크용 함수
# def check_ascendingOrder(s):
#     for i in range(1, len(s)):
#         if ord(s[i]) < ord(s[i-1]):
#             return False
#     return True
#
# # 모음 1개, 자음 2개 체크용 함수
# def check_alphabet(s):
#     moum = ['a', 'e', 'i', 'o', 'u']
#
#     # 모음이 1개라도 s에 포함된다면 and s에서 모음을 다 뺐을 때 길이가 2 이상이라면
#     if any(alpha in moum for alpha in s) and len(set(s)-set(moum)) >= 2:
#         return True
#
# def backTracking(): # DFS를 이용함
#
#     # (1)길이가 충족되고, (2)오름차순이고, (3)모음1개 자음2개가 충족되면
#     if len(tmp) == l and check_ascendingOrder(tmp) and check_alphabet(tmp):
#         for i in tmp:
#             print(i, end='')
#         print()
#         return
#     prev = 0 # 중복 방지용 이전 값
#     for i in range(c): # l개의 숫자가 모이는 과정
#         if prev != lst[i] and not visited[i]:  # 이전값과 현재값이 다르고, 방문안한 경우
#             visited[i] = True  # 방문처리
#             tmp.append(lst[i])  # 현재값 tmp에 넣음 (l개까지 모을거임)
#             prev = lst[i]  # 현재값은 이제 prev값으로 바뀜
#             backTracking()
#
#             # 재귀 호출이 끝나면 방문 여부를 해제 & 마지막으로 추가한 요소를 제거
#             visited[i] = False
#             tmp.pop()
#
# backTracking()