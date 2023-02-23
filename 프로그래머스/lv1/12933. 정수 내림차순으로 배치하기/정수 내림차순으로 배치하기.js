function solution(n) {
    var answer = [];
 
  let str = String(n)
  for(let i = 0; i < str.length; i++){
    answer.push(str[i])

  }
 answer.sort((a,b) => b - a)

  return Number(answer.join(''))
}