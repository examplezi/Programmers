function solution(my_str, n) {
    var answer = [];
   
let a =  my_str.slice(0,n) 
  answer.push(a)
  for(let i = 1; i < my_str.length / n; i++){
     let b = my_str.slice(n * i, n *(i+1))
     answer.push(b)
  }
  return answer
}