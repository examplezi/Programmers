function solution(n) {
    var answer = 0;
 
    for(let i = 1; i < 300 ; i++){
        if((6 * i) % n === 0 ){
            answer = answer + (6 * i)
            break
        }
    }
    return answer / 6
}