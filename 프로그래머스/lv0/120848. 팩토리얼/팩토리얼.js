function solution(n) {
    var answer = 1;
//    return answer;
  for(let i = 1; i <= 10; i++){
    
    answer = answer * i
    console.log(i, answer)
    if(n === answer){
      return i
    }
    else if(n < answer){
      return i - 1
    }
  }
}