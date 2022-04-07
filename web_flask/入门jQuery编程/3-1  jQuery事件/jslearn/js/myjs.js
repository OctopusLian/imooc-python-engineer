$(function() {
	// js业务逻辑和html分离

	// 鼠标单击事件
	// $('div').click(function() {
	// 	alert('点击了')
	// })

	// 双击事件
	// $('div').dblclick(function() {
	// 	alert('点击了2次')
	// });

	$('div').on('dblclick', function() {
		alert('点击了2次')
	})

	// hover
	// $('div').mouseenter(function() {
	// 	$(this).css({
	// 		'background-color': '#f00'
	// 	})
	// }).mouseleave(function() {
	// 	$(this).css({
	// 		'background-color': '#fff'
	// 	})
	// })

	$('div').hover(function(){
		$(this).css({
			'background-color': '#00f'
		})
	}, function() {
		$(this).css({
			'background-color': '#fff'
		})
	})

	// 绑定键盘事件
	$('#username').keyup(function() {
		var val = $(this).val()
		console.log(val)
	})

	// 用户名获得焦点
	$("#uname").focus();
	$("#uname").blur(function() {
		var phone = $(this).val()
		if (phone.length !== 11) {
			$("#txtError").text('输入的手机号码不正确')
		}
	})

	// 性别选择发生变化时触发
	$('#sex').change(function() {
		var sex = $(this).val()
		console.log(sex)
	})

	// 表单提交
	$('form').submit(function() {
		alert('表单提交了')
		// 验证我们的表单
		// 验证通过了，才需要提交表单
		return false; // 阻止表单的提交
	})

	// a标签的事件
	$('.reg2').click(function(event) {
		// 阻止a标签的默认行为
		event.preventDefault()
		alert('a click')
	});

	$('.reg').click(function(event) {
		alert('a click 2')
	})

	// 事件的冒泡
	$('.reg3').click(function() {
		alert('reg3');
	})
	$('.reg3 span').click(function(e) {
		// 阻止事件冒泡
		e.stopPropagation();
		alert('reg3 span')
	})
})