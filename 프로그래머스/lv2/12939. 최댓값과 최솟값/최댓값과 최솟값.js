function solution(s) {
       var answer = [];
   // return answer;
  let arr = s.split(' ')
  arr.sort((a,b) => a - b)
  answer.push(arr[0])
  answer.push(arr[arr.length-1])
  console.log(arr, answer)
  return answer.join(' ')
}