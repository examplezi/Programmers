function solution(t, p) {
    var answer = [];
    let count = 0
  for(let i = 0; i < t.length; i++){
    
    answer.push(t.substr(i,p.length))
    console.log(t.substr(i,p.length))
    if(answer[i].length === p.length && Number(answer[i]) <= Number(p)){
     count ++
  }
  }
    //return answer;
  // 
  
  return count
  
}
