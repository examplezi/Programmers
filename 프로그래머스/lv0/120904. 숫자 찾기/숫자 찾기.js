function solution(num, k) {
    var answer = 0;
  let num1 = num.toString().split('')
  console.log(num1)
  for(let i = 0; i < num1.length; i++){
    if(Number(num1[i]) === k){
      answer = answer + i + 1
    }
  }
    return answer;
}