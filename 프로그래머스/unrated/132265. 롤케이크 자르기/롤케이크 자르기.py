
# def solution(topping):
#     answer = 0  
#     for i in range(1,len(topping)+1):
#         #print(i, set(topping[:i]), set(topping[i:]))
#         brother = set(topping[:i])
#         baby = set(topping[i:])
#         if len(brother) == len(baby):
#             answer += 1
#     return answer
    
    
def solution(topping):
    answer = 0
    #length = len(topping)

    forward = set()
    backward = {}
    for i in topping:
        backward[str(i)] = backward.get(str(i), 0)
        backward[str(i)] += 1
    for i in topping:
        forward.add(i)
        backward[str(i)] -= 1
        if backward[str(i)] == 0:
            del backward[str(i)]
        if len(forward) == len(backward.keys()):
            answer += 1
    return answer