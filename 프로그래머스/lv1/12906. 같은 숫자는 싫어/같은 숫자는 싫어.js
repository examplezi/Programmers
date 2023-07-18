function solution(arr)
{
    var answer = [];
    for(let i =0; i < arr.length; i++){
        if( arr[-1] !== arr[i] ) {
            answer.push( arr[i] )
        }
    }
    
    return answer;
}