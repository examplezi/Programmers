function solution(k, score) {
    var answer = [];
  let record= []
  for(let i = 0; i < score.length; i++){

    answer.push(score[i])
    answer.sort((a,b) => b - a ).splice(k)
    record.push(answer[answer.length-1])
  }
return record
}