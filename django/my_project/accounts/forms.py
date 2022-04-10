import re

from django import forms
from django.db import transaction

from accounts.models import User, UserProfile


class LoginForm(forms.Form):
    """ 登录表单 """
    username = forms.CharField(label='用户名',
                               max_length=100,
                               required=False,
                               help_text='使用帮助',
                               initial='admin')
    password = forms.CharField(label='密码', max_length=200, min_length=6,
                               widget=forms.PasswordInput)

    def clean_username(self):
        """ 验证用户名 hook 钩子函数 """
        username = self.cleaned_data['username']
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern, username):
            raise forms.ValidationError('手机号%s输入不正确',
                                        code='invalid_phone',
                                        params=(username, ))
        return username

    def clean(self):
        data = super().clean()
        print(data)
        # 如果单个字段有错误，直接返回，不执行后面的验证
        if self.errors:
            return
        username = data['username']
        password = data['password']
        # username = data.get('username', None)
        # password = data.get('password', None)
        if username and password:
            # 查询用户名和密码匹配的用户
            user_list = User.objects.filter(username=username)
            err_list = []
            if user_list.count() == 0:
                err_list.append(forms.ValidationError('用户名不存在'))
                # raise forms.ValidationError('用户名不存在')
            # 验证密码是否正确
            # TODO 使用加密算法进行验证
            if not user_list.filter(password=password).exists():
                # raise forms.ValidationError('密码不正确')
                err_list.append(forms.ValidationError('密码不正确'))
            if err_list:
                raise forms.ValidationError(err_list)
        return data


class UserEditForm(forms.Form):
    """ 用户的信息维护 """
    SEX_CHOICES = (
        (1, '男生'),
        (0, '女生'),
    )
    username = forms.CharField(label='用户名',
                               max_length=100,
                               required=False,
                               help_text='使用帮助',
                               initial='admin')
    email = forms.EmailField(label='电子邮箱', max_length=200)
    age = forms.IntegerField(label='年龄')
    sex = forms.ChoiceField(label='性别', choices=SEX_CHOICES,
                            widget=forms.RadioSelect)
    birth_date = forms.DateField(label='生日')
    avatar = forms.ImageField(label='用户头像')


class UserRegForm(forms.Form):
    """ 用户注册表单 """
    username = forms.EmailField(label='用户名', max_length=200, min_length=5)
    password = forms.CharField(label='密码', max_length=200, min_length=6,
                               widget=forms.PasswordInput)
    nickname = forms.CharField(label='用户昵称', max_length=32, required=False)
    birth_date = forms.DateField(label='用户的生日', required=False)


class UserChangeForm(forms.ModelForm):
    """ 从模型创建表单 -- 用户基本信息修改 """
    class Meta:
        model = User
        # fields = ('username', 'password', 'nickname', 'avatar')
        exclude = ('status', )
        labels = {
            'username': '手机号码'
        }
        widgets = {
            'password': forms.PasswordInput(attrs={
                'style': 'border: 1px solid #f00'
            })
        }
        error_messages = {
            'username' : {
                'max_length': '用户名超过了最大长度限制',

            }
        }

    def clean_username(self):
        """ 验证用户名 hook 钩子函数 """
        username = self.cleaned_data['username']
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern, username):
            raise forms.ValidationError('手机号%s输入不正确',
                                        code='invalid_phone',
                                        params=(username, ))
        return username

    @transaction.atomic
    def save(self, commit=False):
        # 得到模型的对象，commit=Flase，并没有提交到数据
        user_obj = super().save(commit)
        # 此处还可以进行一些业务逻辑的处理
        user_obj.save()
        # 对其他模型的一个操作
        UserProfile.objects.create(user=user_obj, username=user_obj.username)
        return user_obj


class AvatarUploadForm(forms.Form):
    """ 用户头像上传 """
    avatar = forms.ImageField(label='用户头像')