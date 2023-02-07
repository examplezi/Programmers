function solution(cipher, code) {
     var answer = [];
  let array = cipher.split("")
 // let arr2 = array.shift()
  console.log(array)
 for(let i=0 ;i <= (array.length) ;i++){
 //  console.log(array[code*i-1],code*i)
   answer.push(array[code*i-1])
 }
    return answer.join("")
}
