function solution(s) {
//   //  var answer = '';
//   //  return answer;
//     //  return s.split('').sort().reverse().join('');
//     //return s.split('').reverse().join('');
//   // 대,소문자를 쪼개서 분리해서 정렬 
//   let lower = []
//   let upper =[]
//  for(let i =0; i < s.length; i++){
//    // console.log(s[i].toUpperCase())
//    // console.log(s[i])
//    if(s[i].toUpperCase() !== s[i]){
//      lower.push(s[i])
//    //  console.log(lower)
//    }else {
//      upper.push(s[i])
//    //  console.log(upper)
//    }
//  }
 
//  let arr = lower.sort((a,b) => b - a).join('')
//  let arr2 = upper.sort((a,b) => b - a).join('')
// // console.log(arr2)
//   console.log(arr, arr2)
// // let arr = s.split('')
// // let arr2 = arr.sort((a,b) => b-a)
// // console.log(arr)
// //   console.log(arr2)
//   return arr + arr2
    return s.split('').sort().reverse().join('');
}