function solution(left, right) {
  let answer = 0;

  for(let i=left; i<=right; i++) {

    let p = 0;
    for(j=1; j<=i; j++) { // 약수 구하기
      if(i%j == 0) p++;
     // console.log(p)
    }

    if(p % 2 == 0) answer += i; // 짝수는 더하고
    else answer -= i; // 홀수는 빼고
  }

  return answer;
}