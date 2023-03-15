function solution(array, commands) {
    const answer = [];
    
    for( let idx = 0; idx < commands.length; idx++ ) {
        const i = commands[idx][0]; // 이중배열의 첫번째값
        const j = commands[idx][1]; // 이중배열의 두번째값
        const k = commands[idx][2]; // 이중배열의 세번째값
        
        const result = array.slice( i - 1, j ) // 0부터 시작(-1)
                            .sort( (a, b) => {
                                return a - b //오름차순
                            })
        answer.push( result[k - 1] ) //인덱스 0부터 시작 
    }
    
    return answer;
}