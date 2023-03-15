function solution(nums) {
    // 가질 수 있는 폰켓몬 수 
    const max = nums.length / 2
    // 중복 제거로 폰켓몬 종류 수 
    const arr = [...new Set(nums)]
    // 내가 가질 수 있는 폰켓몬의 수보다 종류가 더 많으면
    // -> 모든 다른 종류의 폰켓몬을  하나씩 가질 수 있음
    // 내가 가질 수 있는 폰켓몬의 수보다 폰켓몬 종류가 더 적으면
    // -> 최대한 다양한 종류의 폰켓몬을 가지려고 해도 원래 있던 폰켓몬 종류의 수가 최대로 가질 수 있는 폰켓몬 종류의 수
 return   arr.length > max ? max : arr.length
}