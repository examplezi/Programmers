function solution(num, k) {
     let str = String(num)
     if(str.indexOf(k) !== -1){ //일치하는 값이 있다면
        return str.indexOf(k)+1
     }else{
        return str.indexOf(k) 
     }

    
}