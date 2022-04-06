function show1(){
	//alert("123456");
	//document.getElementById("userName").value="imooc";
	var xb=document.getElementsByName("xb");
	var xbText;
	if(xb[0].checked){
		xbText=xb[0].value;
	}else{
		xbText=xb[1].value;
	}
	alert(xbText);
}