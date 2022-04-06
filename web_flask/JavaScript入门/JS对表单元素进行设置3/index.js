function ymd(){
	//获取id=yyyy的控件
	var yyyy=document.getElementById("yyyy");
	var mm=document.getElementById("mm");
	var dd=document.getElementById("dd");
	var date=new Date();
	var year=parseInt(date.getFullYear());
	initSelect(yyyy,1999,year);
	initSelect(mm,1,12);
	initSelect(dd,1,31);
}
/*给列表框赋值，传递三个参数：表单元素，开始值，结束值*/
function initSelect(obj,start,end){
   for(var i=start;i<=end;i++){
		obj.options.add(new Option(i,i));
	}
}