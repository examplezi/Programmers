function solution(my_string) {
  
let regex = /[^0-9]/g; // 정규표현식
let result = my_string.replace(regex, "").split("").map(Number);

  return result.sort()
  
}