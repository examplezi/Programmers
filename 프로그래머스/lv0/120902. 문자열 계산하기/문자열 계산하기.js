function solution(my_string) {
    const arr = my_string.split(" ");
   
    let result = Number(arr[0]);
     console.log(arr, result)
  
    arr.forEach((item, index) => {
        if(item === "+"){ // 인자가 '+'라면
            result += Number(arr[index + 1]); // + 다음의 인자를 더하라
          
        }
        
        if(item === "-"){
            result -= Number(arr[index + 1]);
        }
    })
    
    return result;
}