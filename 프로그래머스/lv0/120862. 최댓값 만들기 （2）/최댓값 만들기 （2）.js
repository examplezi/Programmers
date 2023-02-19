function solution(numbers) {
    let max = numbers[0] * numbers[1];
    
    for(let i = 0; i < numbers.length - 1; i++){ // 마지막 원소 - 1
        const first = numbers[i];
        
        for(let j = i + 1; j < numbers.length; j++){ //마지막 원소까지 
            const second = numbers[j];
            
            if(max < first * second){
                max = first * second;
            }
        }
    }
    
    return max;
}