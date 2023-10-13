# 정렬을 숫자 순
# 1.head 부분 정렬(대소문자 구분 x) -> 소문자로 만든 후 통합,,? 숫자 전까지 
# 2. number 정렬 -> 앞자리의 0 은 무시, 뒤에서부터 추출해서 0이 나올때까지?
# head, number가 같다면 정렬 후에도 기존 자리 유지 
import re
# def solution(files):
#     answer = []
#     head = ""
#     head_list = []
#     small = [i.lower() for i in files]
#     print(small)
#     # 문자열을 돌다 숫자가 나온다면 멈추고 head.append()
#     for name in small:
#         for i in range(len(name)):
#             #print(name[i])
#             if not name[i].isdigit(): #숫자가 아니라면
#                 head += name[i]
#             else: # 숫자라면 
#                 head_list.append(head)
#                 head = ""
#                 break
            
#     print(head_list)
#     print(files)
#     files.sort( key = lambda x : head_list)
#     print(files)
        #letters_only = ''.join(re.findall("[a-zA-Z]", mixed_string))
        #alpha = ''.join(re.findall("[a-zA-Z]", i))
        #print(alpha)

def solution(file_names):
    filt = re.compile(r'([a-zA-Z\-\n\s.]+)([0-9]{0,5})(.*)')


    files = []
    for file_name in file_names:
        files.extend(filt.findall(file_name))
    files.sort(key=lambda x: (x[0].lower(), int(x[1])))
    answer = [''.join(i) for i in files]
    return answer