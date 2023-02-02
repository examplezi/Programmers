function solution(order) {
    let answer = 0;
    let str = String(order)
    for(let i =0; i< str.length; i++){
    if( str[i] === "3"){
        answer++
    }
    if( str[i] === "6"){
        answer++
    }
    if( str[i] === "9"){
        answer++
    }
}    
    return answer;
}