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
	// 获取列表框的长度
	var n=yyyy.length;
	// 列表框选中某一个条目
	yyyy.selectedIndex=Math.round(n/2);
	// 将某个列表框的条目数设置为零，效果是删除
	// dd.options.length=0;
}
/*给列表框赋值，传递三个参数：表单元素，开始值，结束值*/
function initSelect(obj,start,end){
   for(var i=start;i<=end;i++){
		obj.options.add(new Option(i,i));
	}
}

function selectYmd(){
	var yyyy=document.getElementById("yyyy");
	var mm=document.getElementById("mm");
	var dd=document.getElementById("dd");
	var m=parseInt(mm.value);
	var dayEnd;
	if(m==4 || m==6 || m==9 || m==11){
		dayEnd=30;
	}else if(m==2){
		dayEnd=28;
		y=parseInt(yyyy.value);
		if((y % 4==0 && y % 100 !=0) || y % 400 ==0){
			dayEnd=29;
		}
	}else{
		dayEnd=31;
	}
	dd.options.length=0;
	initSelect(dd,1,dayEnd);
}