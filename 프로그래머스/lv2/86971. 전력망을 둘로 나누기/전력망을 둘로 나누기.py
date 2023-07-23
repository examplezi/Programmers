# from collections import Counter, deque

# def solution(n, wires):
#     answer = -1
#     # 1. 노드 중에 가장 많이 언급된거 찾기 (max_count)
#     # ** 연속된 숫자 2개가 나오면 하나의 숫자로 합치기 
#     # 2. 그 노드랑 연결된 모든 노드 하나씩 끊어서 확인해보기 
#     # 3. 끊는 방법 : 인덱스 슬라이싱..? -> set으로 중복 제거 , min(counter 개수 뺀값) 
#     arr = [i for sub in wires for i in sub] # 일차원리스트 
#     counter = Counter(arr)
#     max_count = counter.most_common(1) # (4번노드(기준노드), 4번), (2번노드, 2번), (7번노드, 3번)
#     #print(arr, counter, max_count)
#     linked_list = []
#     for i in range(len(arr)):
#         if i == 0 or arr[i] != arr[i - 1]:
#             linked_list.append(arr[i])
#     #print(linked_list,max_count[0][0])
    
#     standard = max_count[0][0]
#     # for i in range(len(linked_list)):
#     #     if i == standard:
            
            
#     # 언제까지? standard 기준으로 다 끊어봐서 최소값을 리스트에 넣고 min()
#     # before= []
#     # after= []
#     # found_standard = False
#     cut_count = []
#     #while len(linked_list):
#     #print(linked_list)
    

#     cut_count = []
#     # before= []
#     # after= []
#     standard_idx = linked_list.index(standard)
#     print(linked_list,standard,standard_idx)
#     before_standard = list(set(linked_list[:standard_idx]))
#     after = list(set(linked_list[standard_idx :]))
#     before_inc_standard = list(set(linked_list[:standard_idx+1]))
#     after_exc_standard = list(set(linked_list[standard_idx +1:]))
#     if standard in after_exc_standard:
#         after_exc_standard.remove(standard)
#     cut_count.append(abs(len(before_standard) - len(after)))
#     cut_count.append(abs(len(before_inc_standard ) - len(after_exc_standard )))
#     print(before_standard,after)
#     print(before_inc_standard, after_exc_standard)
#     print(cut_count)
#     return min(cut_count)


uf = []

def find(a):
    global uf
    if uf[a] < 0: return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb: return
    uf[pa] += uf[pb]
    uf[pb] = pa

def solution(n, wires):
    global uf
    answer = int(1e9)
    k = len(wires)
    for i in range(k):
        uf = [-1 for _ in range(n+1)]
        tmp = [wires[x] for x in range(k) if x != i]
        for a, b in tmp: merge(a, b)
        v = [x for x in uf[1:] if x < 0]
        answer = min(answer, abs(v[0]-v[1]))

    return answer


            