function solution(s) {
let answer = '';
    let words = s.split(' '); // 길이 3
    
    for (let i = 0; i < words.length; i++) {
        for(let j = 0; j < words[i].length; j++) { //알파벳에 접근
            if(j % 2 === 0) {
                answer += words[i][j].toUpperCase();
            } else {
                answer += words[i][j].toLowerCase();
            }
        }
        if (i < words.length -1) { //공백 추가 
            answer += ' ';
        }
    }
    return answer;
}