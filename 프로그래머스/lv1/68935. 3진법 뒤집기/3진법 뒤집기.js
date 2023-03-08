function solution(n) {
    var answer = [];
  let str = n.toString()
 // console.log(str)
// let str2 = parseInt(str,3)
  let str2 = n.toString(3)
  //let str3 = str2.reverse()
// console.log(str2)
  for(let i = 0; i < str2.length; i++){
    answer.push(str2[i])
  }
answer.reverse()
  let aaa = answer.join('')
  let bbb = parseInt(aaa,3)
  //console.log(answer, aaa, bbb)

    return bbb;
}