# from collections import deque
# def solution(msg):
#     answer = []
#     q = deque()
#     n = len(msg)
#     #msg = deque(msg)
#     alpha = {'A': 1, 'B':2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P':16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X' :24, 'Y': 25, 'Z': 26 }
#     #while len(msg) > 0:
        
#     for i in range(n): # 0-4
#         if msg[i:i+2] not in alpha:
#             answer.append(alpha[msg[i]])
#             alpha.update({msg[i:i+2] : 27+i})
#             #msg.pop()
#         #print(msg[i:i+2])
#         else: # 만약 사전에 있다면
#             answer.append(alpha[msg[i:i+2]])
#             alpha.update({msg[i:i+3] : 27+i})
            
#             msg = msg[:i] + msg[i+3:]
#             #new_string = my_string[:a] + my_string[b+1:]
#     print(alpha)
#     print(answer)


def solution(msg):    
    dict = {}

    for num in range(0, 26):
        alpha = chr(num + 65)
        dict[alpha] = num + 1

    # A ~ Z 사전을 만들어준다.


    answer = [0]
    value = 26
    base = ""

    for i in range(len(msg)):
        base += msg[i]
        if not base in dict:
            value += 1
            dict[base] = value

            base = msg[i]
            answer.append(dict[base])
            # 사전에 없다면 사전에 추가하고, base를 msg[i]로 변경한다.
        else:
            answer[-1] = dict[base]
            # base가 사전에 있다면 answer에 마지막으로 추가한 숫자를 변경해준다.


    return answer