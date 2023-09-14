# 
def solution(absolutes, signs):
    answer = 123456789
    for i in range(len(absolutes)):
        #print(absolutes[i], signs[i])
        if signs[i] == False:
            absolutes[i] *= -1
        else:
            continue
    #print(absolutes)
    return sum(absolutes)
  