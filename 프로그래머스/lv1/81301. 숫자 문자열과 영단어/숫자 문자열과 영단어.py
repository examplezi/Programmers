def solution(s):
    answer = s.replace('one','1').replace('seven','7').replace('eight','8').replace('two','2').replace('three','3').replace('four','4').replace('five','5').replace('six','6').replace('nine','9').replace('zero','0')
    return int(answer)