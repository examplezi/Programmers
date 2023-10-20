from collections import defaultdict
def solution(tickets):
    answer = []
    book = defaultdict(list)
    for start, end in tickets:
        book[start].append(end)
    print(book)
    
    for key in book.keys():
        book[key].sort()
    print(book)
    
    route = ["ICN"]
    final = []
    while route:
        now = route[-1]
        
        if book[now] != []:
            route.append(book[now].pop(0))
        else: #비었다면
            final.append(route.pop())
    return final[::-1]