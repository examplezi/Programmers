# 두 가지를 비교해서 서로 같으면 pop, 아니면 남긴다 -> stack 
def solution(s):
    tmp = []
    
    for i in s:
        if not tmp:
            tmp.append(i)
        elif i == tmp[-1]:
            tmp.pop()
        else:
            tmp.append(i)
            
    if len(tmp) >0:
        return 0
    else:
        return 1