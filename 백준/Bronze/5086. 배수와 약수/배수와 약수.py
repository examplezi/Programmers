import sys
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        #print(a + b)
        if b % a == 0:
            print("factor")
        elif a % b == 0:
            print("multiple")
        else:
            print("neither")
    except:
        break