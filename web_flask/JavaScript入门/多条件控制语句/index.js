/*
  成绩是100分，显示满分
  成绩大于等于90，显示优秀
  成绩大于等于70，显示良好
  成绩大于等于60，显示及格
  否则，不及格
*/
var myscore=40;
var str;
var n=parseInt(myscore/10);
switch(n){
	case 10:
 		str="manfen";
 		break;
 	case 9:
 		str="youxiu";
 		break;
 	case 8:
 	case 7:
 		str="lianghao";
 		break;
 	case 6:
 		str="jige";
 		break;
 	default :
 		str="bujige";
 		break;
}
console.log(str);

