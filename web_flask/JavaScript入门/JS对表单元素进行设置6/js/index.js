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
// 删除列表框的某一个条目。即：按索引号删除
function deleteSelect(){
	var dd=document.getElementById("dd");
	//dd.options.remove(1);
	for(i=dd.length;i>=0;i--){
		dd.options.remove(0);
	}
}
//完成作业：第二种方法实现年月日的三级联动

function initLogo(){
	var logo=document.getElementById("logo");
	for(i=1;i<=15;i++){
		logo.options.add(new Option(i,i));
	}
}

function selectLogo(){
	var logo=document.getElementById("logo");
	var n=logo.value;
	var logoImg=document.getElementById("logoImg");
	logoImg.src="image/headLogo/"+n+".gif";
}