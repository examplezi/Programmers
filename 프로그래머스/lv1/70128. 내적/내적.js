function solution(a, b) {
  let answer = 0
  for(let i =0; i < a.length; i++){
    for(let j =0; j < b.length; j++){
        
      while(i===j){
        answer+= a[i] * b[j]
        break
      }
    }
  
  }
  return answer
    
}