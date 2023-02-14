function solution(n) {
    var answer = 0
    
    for(let i = 1; i <= n; i++) {
        let cnt = 0
        for(j = 1; j <= i; j++) {
            if(i % j === 0)
              cnt ++
          console.log(i,j, cnt)
        }
        
        if(cnt > 2) { // 약수가 3 이상
            answer += 1
        }
    }
    
    return answer
}