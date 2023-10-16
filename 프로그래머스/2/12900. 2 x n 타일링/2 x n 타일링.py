import math
def solution(n):
    answer = 0
    maxnum=n//2
    count1=1
    count2=2
    if n==1:
        return count1
    elif n==2:
        return count2
    for i in range(n-2):
        temp=count1
        count1=count2
        count2=count1+temp
    answer=count2%1000000007
    return answer