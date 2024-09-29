def solution(sent):
    sent = list(sent)
    stack = []
    for c in sent:

        # 스택이 비어있으면 append
        if len(stack) == 0:
            stack.append(c)
            continue

        if stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return int(len(stack)==0)

print(solution("baabaa")) # 1
print(solution("cdcd")) # 0