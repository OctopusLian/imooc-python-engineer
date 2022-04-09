import re

from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField, FileField
from wtforms.validators import DataRequired, ValidationError


def phone_required(form, field):
    """ 自定义的手机号码的验证 """
    # 强制验证用户名为手机号
    username = field.data
    pattern = r'^1[0-9]{10}$'
    if not re.search(pattern, username):
        raise ValidationError('请输入手机号码')
    return field


class LoginForm(FlaskForm):
    """ 登录表单的实现 """
    username = StringField(label='用户名', default='admin', validators=[phone_required])
    password = PasswordField(label='密码')
    submit = SubmitField('登录')


class RegisterForm(FlaskForm):
    """ 用户注册表单 """

    # def __init__(self, csrf_enabled, *args, **kwargs):
    #     super().__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

    username = StringField(label='用户名', default='')
    password = PasswordField(label='密码', validators=[DataRequired('请输入密码')])
    birth_date = DateField(label='生日')
    age = IntegerField(label='年龄')
    submit = SubmitField('注册')

    def validate_username(self, field):
        """ 验证用户名 """
        # 强制验证用户名为手机号
        username = field.data
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern, username):
            raise ValidationError('请输入手机号码')
        return field

    # def validate(self):
    #     pass


class UserAvatarForm(FlaskForm):
    """ 用户头像上传 """
    avatar = FileField(label='上传头像', validators=[
        FileRequired('请选择头像文件'),
        FileAllowed(['png'], '仅支持PNG图片上传')
    ])