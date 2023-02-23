function solution(n) {
    var answer = [];
    let arr = String(n).split("").reverse()
  for(let i = 0; i < arr.length; i++){
    answer.push(Number(arr[i]))
  }

 
   return answer;
}