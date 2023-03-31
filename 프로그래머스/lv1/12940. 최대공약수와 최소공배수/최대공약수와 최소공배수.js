function solution(n, m) {
  let answer = []
  
  let G = 0;
  let L = 0;
    
    
    let num = n > m ? n : m;
    
    for(let i = 1; i <= num; i++){
        if(n % i === 0 && m % i === 0){
            G = i
        }
    }
    
    L = n * m / G
    answer = [G,L]

    return answer 
    
}