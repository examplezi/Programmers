function solution(my_string) {
   let str = my_string;
    str = str.replaceAll("a","")   
    str = str.replaceAll('e',"")
    str = str.replaceAll('i',"")
    str = str.replaceAll("o","")
    str = str.replaceAll("u","")

    return str
}