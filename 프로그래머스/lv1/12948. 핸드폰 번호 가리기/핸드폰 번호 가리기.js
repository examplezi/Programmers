function solution(phone_number) { 
let answer = phone_number.slice(-4)
  console.log(answer)
 let result = "*".repeat(phone_number.length-4)
 return result + answer


}