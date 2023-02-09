function solution(array) {
 
  let sum = 0;
  let arr = array.join('')
  for(let i = 0; i < arr.length; i++){
    if(arr[i] === '7'){
      sum ++
    }
  }
  return sum
}