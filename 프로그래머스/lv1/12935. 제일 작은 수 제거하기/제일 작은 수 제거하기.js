function solution(arr) {
    var answer = [];
    let min = arr[0]
    for (i = 1; i < arr.length; i++){
        if(arr[i] < min) {
            min = arr[i]
        }
    }
    for(i = 0; i < arr.length ; i++){
        if(arr[i] !== min) {
            answer.push(arr[i])
        }
    }
    
    return answer.length === 0 ? [-1] : answer;
}