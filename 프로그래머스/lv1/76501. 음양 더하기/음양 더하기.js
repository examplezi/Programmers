function solution(absolutes, signs) {
    
  let result = 0
  
  for(let i = 0; i < absolutes.length; i++){
    for(let j = 0; j < signs.length; j++){
      if( i === j && signs[j] === true){
          result = result + absolutes[i]
         
      }
      else if( i === j && signs[j] === false){
        result = result - absolutes[j]
      }
     
    }
    
  }
  return result
}