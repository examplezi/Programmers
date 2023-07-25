
# lost , reserve에 둘 다 있다면 reserve.pop() 해당요소 제거 
def solution(n, lost, reserve):
    answer = 0
    check = [0] * n
    # list1과 list2의 교집합 구하기
    intersection = list(set(lost) & set(reserve))
    # list2에서 교집합에 해당하는 값 제거
    reserve = [x for x in reserve if x not in intersection]
    lost = [x for x in lost if x not in intersection]
    lost.sort()
    reserve.sort()
    print(check)
    
    for idx in reserve:
        check[idx-1] = 2
    print("여분 가지고 있는 애들",check)
    
    # for idx in lost:
    #     if idx 
    #     check[idx-1] = 1
    # print(check)
    for idx in range(len(check)):
        if idx+1 not in lost and check[idx] == 0:
            check[idx] = 1
    print("로스트에 없는 애들 1로 업데이트",check)
    #check에 0이 있고 그 인덱스 +1이 lost의 요소와 같고 
    
    for i in range(len(check)):
        print(i,check[i])
    for idx in lost: # 앞번호가 빌려주기 
        # if idx > len(check)-1:
        #     continue #가 check의 인덱스 범위를 넘어버리면 continue
        if idx -2 >= 0 and check[idx-1] ==0 and check[idx-2] ==2: #idx가 1부터기 때문에 오류남 
            check[idx-1] = 1
            check[idx-2] =1
        elif idx <= len(check)-1 and check[idx-1] ==0 and check[idx] ==2: # not in 
            check[idx-1] = 1
            check[idx] =1
    print("앞번호가 빌려주기",check)
        
        
        
        
        
        
    return check.count(1) + check.count(2)