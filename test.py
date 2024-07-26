lst = ['l', 'o', 'v', 'e']

moum = ['a', 'i', 'e', 'o', 'u']

tt = ['a', 'c', 't', 'w']
s = lst

def check_alphabet(s):
    moum = ['a', 'i', 'e', 'o', 'u']

    # 모음이 1개라도 s에 포함된다면 and s에서 모음을 다 뺐을 때 길이가 2 이상이라면
    if any(alpha in moum for alpha in lst) and len(set(s)-set(moum)) >= 2:
        return True

print(check_alphabet(['a', 'b', 't', 'w']))

print(any(alpha in moum for alpha in lst))