function solution(numbers, direction) {
    var answer = [];
  //  return answer;
    if(direction == "right"){
       let last = numbers.pop()
      answer.push(last)
      // console.log(answer)
      // console.log(numbers)
      return answer.concat(numbers)
    }
     else{
        let first = numbers.shift()
        answer.push(first)
      return numbers.concat(answer)
    }
}