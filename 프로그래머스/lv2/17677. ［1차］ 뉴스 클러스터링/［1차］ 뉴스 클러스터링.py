def solution(str1, str2):
    answer1 = []
    answer2 = []
    inter = []
    str1 = str1.lower()
    str2 = str2.lower()
    #print(str1, str2)
    # 2개씩 끊어서 len() 으로 비교
    # 공백 제거, 영문자만 유효 
    for i in range(len(str1)-1):
      
        if str1[i:i+2].isalpha(): 
            answer1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            answer2.append(str2[i:i+2])
    print(answer1)
    print(answer2)

    copy1 = answer1.copy()
    copy2 = answer2.copy()
    print("copy1",copy1)
    for i in copy1:
        if i in copy2:
            print("교집합 요소",i)
            inter.append(i)
            copy2.remove(i)
    print("교집합",inter)
    
    # 합집합 구하기
    union = answer1 + answer2 #- inter
    #- 연산자는 두 개의 리스트에서 같은 원소들을 제거하는 연산이 아닌, 숫자 간의 빼기 연산을 수행하는 연산자
    print("합집합",union)
    inter2 = inter.copy()
    # for문 통해서 inter와 같다면 remove 
    for i in union:
        if i in inter:
            union.remove(i)
            inter.remove(i)

    print("최종합집합",union)
    print(inter2)
    
        # 자카드 유사도 계산
    if len(union) == 0:
        return 65536
    else:
        return int((len(inter2) / len(union)) * 65536)
    
#     # 두 리스트의 합집합을 구하기 위해 extend() 메소드 사용
#     uni = answer1.copy()
#     uni.extend(x for x in answer2 if x not in answer1)
#     print(uni)
#     print((len(inter) / len(uni)) * 65536)
#     return int(((len(inter) / len(uni)) * 65536))