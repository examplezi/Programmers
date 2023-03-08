function solution(d, budget) {
    var answer = 0;
    //return answer;
  let count = 0
 d.sort((a,b) => a-b)
  console.log(d)
  for(let i =0; i < d.length; i++){
  console.log(d[i])
    if(budget === 0 || d[i] > budget){
      break
    }
  budget = budget - d[i] 
    count++
    console.log(count)
    
  }
  return count
  
  
}