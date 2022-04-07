<!--
 * @Author: zhangniannian
 * @Date: 2022-04-07 13:27:57
 * @LastEditors: zhangniannian
 * @LastEditTime: 2022-04-07 13:37:15
 * @Description: 请填写简介
-->
# 前端开发在线问答系统  

## 问题列表及列表项  

- Flash消息闪现：提示框  
- 轮播图展示  
- 分类菜单:“推荐、关注”等标签页切换效果  
- 问题列表：使用Flex布局  

## 问题底部菜单  

- 固定顶部菜单栏  
- 底部菜单布局：使用Flex布局  
- 问题列表底部菜单图标  
- “阅读原文”收起效果  

## 写文章(提问)页面  

- 预览本地选择好的图片文件  

```js
var reader = new FileReader();
reader.onload = function () { $('.upload-file').css('background-image', 'url(' + reader.result + ')')}
reader.readAsDataURL(file);
```

## 作业  

- 页面的布局:顶部导航、问题描述、问题底部菜单、回答及底部菜单、评论列表、评论回复  
- JS效果:问题简述与详细切换、回复评论输入框的显示  

## 知识点总结  

- CSS布局(relative,absolute,fixed, flex)  
- BootStrap:栅栏布局、组件、全局CSS样式、JS插件  
- jQuery:选择器、事件、操作DOM  

## 课程总结  

- 如何实现想要的功能——不要重复发明轮子  
- 让代码更加容易维护——公共CSS/JS的编写  
- 如何提升编程效率——多看文档  
- 我要背下来吗——初学要理解，用多了自然就记得了  
- 如何才能走向“精通”——扎实的基础