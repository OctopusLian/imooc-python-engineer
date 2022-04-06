 var n=9;
function fun1(){
	var n1=5;//局部变量
	var n=12;//使用全局变量n
	// console.log(n1);
}
function fun2(){
	n=n-1;
}
function fun3(){
	console.log(n);
	console.log(n1);
}
fun1();
fun2();
fun3();
