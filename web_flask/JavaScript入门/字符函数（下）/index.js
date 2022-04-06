var str="aa,ttt,121,gg,ttt,kk,aa,bb,ttt";
var arr=str.split(",");
console.log(arr[0]);
console.log(str.concat(",55",",77",",00"));
console.log(arr.concat("55","77","00"));

var str1=str.replace("aa","imooc");
var str2=str1.replace("aa","imooc");
console.log(str2);
