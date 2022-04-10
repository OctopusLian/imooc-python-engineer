from django.db import models


class CommonModel(models.Model):
    """ 自定义模型的基类 """
    created_at = models.DateTimeField('添加时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)

    class Meta:
        # 抽象类，这个类，并不会生成对应的数据库表
        abstract = True


class User(CommonModel):
    """ 用户基本信息 """
    USER_STATUS = (
        (1, '正常'),
        (0, '删除'),
    )
    username = models.CharField('用户名', max_length=128, unique=True)
    # username = models.CharField('用户名', max_length=128, unique=True, editable=False)
    password = models.CharField('密码', max_length=256)
    nickname = models.CharField('用户昵称', max_length=256, null=True, blank=True)
    avatar = models.ImageField('用户头像', upload_to='avatar/%Y%m', null=True, blank=True)
    status = models.SmallIntegerField('用户状态', default=1, choices=USER_STATUS)
    is_super = models.BooleanField('是否为超级用户', default=False)
    created_at = models.DateTimeField('注册时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    # users = models.Manager()

    class Meta:
        db_table = 'accounts_user'

    def __str__(self):
        return 'User: {}'.format(self.username)


class UserProfile(CommonModel):
    """ 用户详细信息 """
    SEX_CHOICES = (
        (0, '未知'),
        (1, '男'),
        (2, '女'),
    )
    user = models.OneToOneField(User, verbose_name='关联用户',
                                related_name='profile',
                                on_delete=models.CASCADE)
    username = models.CharField('用户名', max_length=128, unique=True)
    real_name = models.CharField('真实姓名', max_length=128, null=True, blank=True)
    sex = models.SmallIntegerField('用户性别', default=0, choices=SEX_CHOICES)
    maxim = models.CharField('用户格言', max_length=128, null=True, blank=True)
    address = models.CharField('用户地址', max_length=128, null=True, blank=True)

    class Meta:
        db_table = 'accounts_user_profile'


class LoginHistory(models.Model):
    """ 用户的登录历史 """
    user = models.ForeignKey(User, related_name='login_history_list',
                             on_delete=models.CASCADE,
                             verbose_name='关联的用户')
    username = models.CharField('用户名', max_length=128)
    login_type = models.CharField('账号平台', max_length=128)
    ip = models.CharField('IP地址', max_length=32, default='')
    ua = models.CharField('登录来源', max_length=128, default='')
    created_at = models.DateTimeField('登录时间', auto_now_add=True)

    class Meta:
        db_table = 'accounts_login_history'
        ordering = ['-created_at']
