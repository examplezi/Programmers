const fs = require('fs');
const [A, B] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const num1 = parseInt(A);
const num2 = B.split('').map(Number); // [3, 8, 5]
let result = num2.reverse().map((x) => x*num1); // [5*num1, 8*num1, 3*num1]
result.push(num1*parseInt(B)); // [5*num1, 8*num1, 3*num1, num1*parseInt(B)]

console.log(result.join('\n'));
// 5*num1
// 8*num1
// 3*num1
// num1*parseInt(B)