def solution(s):
    answer = []
    zero_sum = 0
    cnt = 0
    # return answer        
    while len(s) > 1:
        a = s.replace('0','')
        zero_sum += (len(s) - len(a))
        #print(a,zero_sum)
        cnt += 1
        s = bin(len(a))[2:]
        print(a,zero_sum,cnt,s)
    #s == a

    return [cnt, zero_sum]
    # answer.remove('0')
    # print(answer)
    #print(bin(6)[2:])