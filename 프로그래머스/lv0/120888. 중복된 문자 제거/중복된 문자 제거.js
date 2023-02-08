function solution(my_string) {
    var answer = [];
  let arr = my_string.split('')
 
  for(let i =0; i < arr.length; i++){
    //answer에 포함되어 있지 않다면 
    if(answer.includes(arr[i]) == false)
    answer.push(arr[i])
  }
  return answer.join("")
}