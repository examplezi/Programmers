def solution(sizes):
    answer = 0
    #return answer
    for i in range(len(sizes)):
        #print(sizes[i][0],sizes[i][1])
        if sizes[i][1] >= sizes[i][0]:
            sizes[i][0],sizes[i][1] = sizes[i][1],sizes[i][0]
            #print(sizes[i][0],sizes[i][1])   
    
    
    width = max(sizes, key = lambda x : x[0])
    height = max(sizes, key = lambda x : x[1])
    print(width[0], height[1])
    return width[0] * height[1]
