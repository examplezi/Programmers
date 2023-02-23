function solution(x) {
    var answer = true;

  let sum = 0
  let str = String(x)
  for(let i = 0; i < str.length; i++){
    sum += Number(str[i])

  }
  
   if( x % sum === 0){
      return answer
    }
    else {
      return false
    }
  
}