const fs = require('fs');
const input = fs.readFileSync(process.stdin.fd).toString().split('\n');

 for (let i = 0; i < input.length - 1 ; i++) {
 const Numbers = input[i];
 let arr = Numbers.split(" ");
 let A = parseInt(arr[0]);
 let B = parseInt(arr[1]);
 
 console.log(Number(A+B));
}
