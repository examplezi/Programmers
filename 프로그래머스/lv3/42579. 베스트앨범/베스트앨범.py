# import collections
# def solution(genres, plays):
#     answer = []
#     #fave = collections.Counter(genres)
   
#     result = [[g, p] for g, p in zip(genres, plays)]
#     #fave = collections.Counter([result[i][0] for i in range(len(result))])
#     print(result)
    
#     genre_dict = collections.defaultdict(int)

#     for item in result:
#         genre = item[0]
#         value = item[1]
#         genre_dict[genre] += value

#     sum =  [[genre, value] for genre, value in genre_dict.items()]
#     print(sum)
#     #return answer


from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    genres_order = defaultdict(int)
    genres_plays = defaultdict(list)
    
    for i, (genre, v) in enumerate(zip(genres, plays)):
        genres_order[genre] += v
        genres_plays[genre].append((i, v))
        
    for genre, _ in sorted(genres_order.items(), key = lambda x: x[1], reverse = True):
        for i, v in sorted(genres_plays[genre], key = lambda x: x[1], reverse = True)[:2]:
            answer.append(i)
    
    return answer