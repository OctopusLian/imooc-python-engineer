var d1=new Date();
var d2=new Date("2020-1-1");
console.log(d1.getDate());
console.log(d1.getMonth()+1);//从0开始，0-11
console.log(d1.getFullYear());
console.log(d1.getHours());
console.log(d1.getMinutes());
console.log(d1.getSeconds());
var n=d2.getTime()-d1.getTime();
console.log(parseInt(n/(24*3600*1000)));
//2020-1-1 15:58   日期格式化

function fun_FmtDate(){
  var d1=new Date();
  var yyyy,mm,dd,hh,mi,ss;
  var time;
  yyyy=d1.getFullYear()
  mm=d1.getMonth()+1;
  dd=d1.getDate();
  hh=d1.getHours();
  mi=d1.getMinutes();
  ss=d1.getSeconds();
  time=yyyy+"-"+mm+"-"+dd+" "+hh+":"+mi+":"+ss;
  return time;
}
console.log(fun_FmtDate());