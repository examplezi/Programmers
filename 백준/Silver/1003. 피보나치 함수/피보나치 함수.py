t = int(input())
zero = [1,0,1] # n이 0,1,2 일 때 0이 필요한 횟수
one = [0,1,1] # n이 0,1,2 일 때 1이 필요한 횟수 

def fibo(n) : #[0,1,3]
    if len(zero) <= n : # 3보다 클 떄
        for i in range(len(zero), n+1) :
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[n],one[n])

for i in range(t) : #[3]
    a = int(input()) #[0,1,3]
    fibo(a)