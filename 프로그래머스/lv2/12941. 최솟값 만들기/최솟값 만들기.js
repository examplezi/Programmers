function solution(A,B){
    var answer = 0;
  A.sort((a,b) => a - b );
  B.sort((a,b) => b - a);
 // console.log(A,B)
  for(let i =0; i < A.length; i++){
    for(let j =0; j < B.length ; j++){
      if(i === j){
        answer += A[i] * B[j];
      }
    }
  }
  return answer;
}