function solution(i, j, k) {
    var answer = '';
  let sum= []
  let char = String(k)
 // console.log(char)
//  let sum = 0;
   // return answer;
  for(let a = i; a <= j; a++){
   // console.log(a)
    answer += a
   // console.log(a)
  }
let arr = answer.split('')
 // console.log(arr)
  for(let b = 0; b < arr.length; b++){
  // console.log(arr[b])
     if(arr[b].includes(char)){
   sum.push(arr[b])
 // console.log(sum)
  }
  }
  
  return sum.length
}