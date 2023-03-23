function solution(food) {
    let answer1 = '';
  let answer2 = ''
   // return answer;
  for(let i = 1; i < food.length; i++){
   answer1 = answer1 + String(i).repeat(Math.floor(food[i] / 2))
}
  console.log(answer1)
  return answer1 + "0"+ [...answer1].reverse().join('')
//solution([1, 3, 4, 6])
}