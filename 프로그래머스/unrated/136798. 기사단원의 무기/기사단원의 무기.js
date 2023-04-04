function solution(number, limit, power) {
    const divisors = []; // 약수의 갯수 순서
    
    const getDivisors = (num) => { // 약수구하는 공식을 수정했다
        const tempDivisors = [];
        for(let i = 1 ; i <= num/2 ; i++){
            if(num % i === 0) tempDivisors.push(i);
        }
        return [...tempDivisors, num];
    }
    
    for(let i=1; i<=number; i++){ //약수의 갯수만큼 푸시
        divisors.push(getDivisors(i).length);
    }
    
    const answer = divisors.reduce((acc, res)=>{
        res > limit ? acc+=power : acc+=res
        return acc
    })
    
    return answer
  
    // return answer;
}