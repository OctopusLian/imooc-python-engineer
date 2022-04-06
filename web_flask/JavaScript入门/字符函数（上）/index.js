var str="520134199906061224";
console.log(str.substr(6,4));//起始位置，长度
console.log(str.substring(6,10));//起始位置，结束位置
var n=parseInt(str.charAt(16))
if(n % 2==0){
	console.log("nv");
}else{
	console.log("nan");
}
console.log(str.length);
console.log(str.indexOf(1,4));

