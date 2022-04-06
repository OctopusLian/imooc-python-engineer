var flag=true;
function checkInterest(){
	var interest=document.getElementsByName("interest");
	for(i=0;i<interest.length;i++){
		interest[i].checked=flag;
	}
	if(flag){
		document.getElementById("btn1").value="全不选";
	}else{
		document.getElementById("btn1").value="全选";
	}
	flag=!flag;//开关变量
}

function checkInterest1(){
	var interest=document.getElementsByName("interest");
	for(i=0;i<interest.length;i++){
		interest[i].checked=!interest[i].checked;
		console.log(interest[i].value);
	}
}