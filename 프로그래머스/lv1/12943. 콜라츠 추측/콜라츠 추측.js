function solution(num) {
    let count = 0;
    
    for( let i = 0; i < 500; i++ ) {
        if( num === 1 ) {
            return count
        }
        count++;
        
        num = num % 2 === 0 //짝수라면
                ? num / 2
                : (num * 3) + 1
    }
    return -1;
}