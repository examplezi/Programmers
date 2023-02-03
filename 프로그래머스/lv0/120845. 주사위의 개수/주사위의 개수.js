function solution(box, n) {

       let length = box[0]
       let width = box[1]
       let height = box[2]
     let a =  Math.floor(length / n)
     let b = Math.floor(width / n)
     let c = Math.floor(height / n)
       console.log(a,b,c)
       return a * b * c

}