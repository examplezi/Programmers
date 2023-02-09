function solution(s) {
    var answer = 0;
 
 let arr= s.split(' ').map(Number)

  for(let i = 0; i < arr.length; i++){
     if(Number.isNaN(arr[i]) == false){
        answer = answer + arr[i]
    }
     else {
      answer = answer - arr[i-1]
     }
   }

 return answer
}