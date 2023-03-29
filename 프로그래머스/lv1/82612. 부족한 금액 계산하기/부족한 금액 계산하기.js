function solution(price, money, count) {
    var answer = -1;
  let sum = 0
for(let i = 1; i <= count ; i++){
  console.log(price * i)
  sum += price * i
  console.log(sum)
}
  if(money >= sum) {
    return 0
  }
  else {
    return sum - money
  }
  //  return answer;
}