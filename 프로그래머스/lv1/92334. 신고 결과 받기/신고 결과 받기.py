def solution(id_list, report, k):
    dic = {} # 신고 당한 dict
    mail = []
    report = list(set(report))
    #id = dict(zip(report, 0))
    report = [name.split() for name in report]
    #print(report)
 
    
    for i in id_list:
        if i not in dic:
            dic[i] = 0
    dic2 = dic.copy()
    #print(dic, dic2)
    for i in range(len(report)):
        if report[i][1] in dic:
            dic[report[i][1]] += 1
    #print(dic, dic2)
    
    # 딕셔너리의 값이 k 이상이면 (신고당한 횟수가 이상이면) 
    for i in id_list:
        if dic.get(i) >= k:
            mail.append(i)
    #print(mail) # 프로도, 네오 
    # 리포트 순회해서 리포트의 두번째 값이 mail에 들어있다면 dic2의 값 +1
    for i in range(len(report)):
        if report[i][1] in mail:
            dic2[report[i][0]] += 1
    #print("메일",dic2, dic2.values())
    return list(dic2.values())
    
    # dict 형태로 갱신되게 만들기 
    # 한 유저가 다른 한 유저를 여러 번 신고해도 갱신되지 않음 -> set으로 중복값 없애기 
    # 값이 k와 같으면 