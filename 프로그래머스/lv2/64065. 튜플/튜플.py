import ast

def solution(s):
    answer = []
    s = s[:-2].replace('{','').replace(',',' ').split('}')

    s = [i.split() for i in s]

    s.sort(key=lambda x:len(x))

    for tup in s:
        diff = set(tup) - set(answer)
        answer.append(list(diff)[0])

    answer = [int(i) for i in answer]

    return answer
  
   # 그냥 가장 긴거 찾아서 그거 안의 원소 다 answer에 넣음 되는거 아님..? 
    # arr = s.replace('{', '[').replace('}', ']')
    # print(arr, len(arr))
    # #print(type(new_string))
    # #print(set(arr))
    # arr2 = list(arr)
    # print(arr2)
    # #answer = [[] for _ in range(len(arr2))]
    # answer = []
    # print(answer)
    # # print(arr2)
    # for i in range(2,len(arr2)-2):
    #     print(i,arr2[i])
    #     if i == ',' or i == ']' or i == '[':
    #         continue
    #     answer[i].append(i)
    # # print(answer)