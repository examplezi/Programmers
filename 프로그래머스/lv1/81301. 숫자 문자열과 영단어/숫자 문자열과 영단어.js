function solution(s) {
  var answer = 0;
  //  return answer;
  answer = s.replaceAll('one','1').replaceAll('seven','7').replaceAll('eight','8').replaceAll('two','2').replaceAll('three','3').replaceAll('four','4').replaceAll('five','5').replaceAll('six','6').replaceAll('nine','9').replaceAll('zero','0')
  
  return Number(answer)
}