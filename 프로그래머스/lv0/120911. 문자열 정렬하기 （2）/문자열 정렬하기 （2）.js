
function solution(my_string) {
  
  let small = my_string.toLowerCase()

  let arr = small.split("")

  return arr.sort().join("");
}