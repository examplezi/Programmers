function solution(n) {
let answer = 0
let arr = new Array(n+1).fill(true)
//console.log(arr)
for(let i = 2; i <=n ; i++){
 //console.log(arr[i])
  // if(arr[i] === false){
  //   continue;
  // }
  for(let k = i * 2; k <= n; k += i){
    arr[k] = false
  }
}
 for(let i = 2; i <=n ; i++){
   if(arr[i] === true)
   answer++
 } 
  return answer
}