function solution(num) { 

for( let i = 0; i < 500; i++ ) {
       if(num%2==0){
      num = num/2;
    }
    else if(num==1){
        return i;
    }
    else if(num%2==1){
      num = (num*3)+1;
    }
  }
    return -1;
}

// function solution(num) { 

// for( let i = 0; i < 500; i++ ) {
//        if(num%2==0){
//       num = num/2;
//     }
//     else if(num==1){ // 최종 횟수 반환 
//         return i;
//     }
//     else if(num%2==1){ // 홀수
//       num = (num*3)+1;
//     }
//   }
//     return -1;
// }
