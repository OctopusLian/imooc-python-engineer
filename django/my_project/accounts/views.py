import os

from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from accounts.forms import LoginForm, UserEditForm, UserRegForm, UserChangeForm, AvatarUploadForm
from accounts.models import User, UserProfile


def query_course(request):
    c = request.GET.get('c', None)
    query = Q()
    if c is not None:
        query = query & Q()
    sort = request.GET.get('sort', None)
    if sort is not None:
        query = query & Q()


def user_info(request):
    """ 用户详情-查询优化 """
    user = User.objects.get(pk=1)
    # profile_list = UserProfile.objects.all()
    profile_list = UserProfile.objects.all().select_related('user')

    # 使用SQL查询
    user_list = User.objects.raw('SELECT * FROM  `accounts_user`')
    return render(request, 'user_info.html', {
        'user': user,
        'profile_list': profile_list,
        'user_list': user_list
    })


def user_list_slice(request):
    """ 分页-使用切片 """
    page = request.GET.get('page', 1)
    try:
        page = int(page)
    except:
        # 出现异常默认设置为第一页
        page = 1
    # 每页放多少条数据
    page_size = 10
    # user_list = User.objects.all()[0: 10]
    # user_list = User.objects.all()[10: 20]
    start = (page - 1) * page_size
    end = page * page_size
    user_list = User.objects.all()[start: end]
    return render(request, 'user_list_slice.html', {
        'user_list': user_list
    })


def user_list_paginator(request):
    """ 分页-使用分页器 """
    page = request.GET.get('page', 1)
    user_list = User.objects.all()
    # 第一步，取得分页器
    p = Paginator(user_list, 15)
    # 第二步，取得某一页的对象（实例）
    # page_data = p.get_page(page)
    try:
        page_data = p.page(page)
    except EmptyPage as e:
        print('页面不存在')
        raise Http404
    except PageNotAnInteger as e:
        print('无效的页码')
        raise Http404

    return render(request, 'user_list_paginator.html', {
        'page_data': page_data
    })


class UserListView(ListView):
    """ 分页处理, 面向对象 """
    # 对应的模板
    template_name = 'user_list_class.html'
    # 对应的ORM模型
    model = User
    # 页面大小
    paginate_by = 20
    # 获取页面的参数（当期第几页）
    page_kwarg = 'p'


def user_register(request):
    """ 用户注册 """
    # 1. 获取表单的数据
    # 2. 验证数据是否符合要求
    # 3. 添加用户信息（用户基本信息、详细信息）
    username = '13000000002'
    try:
        user = User.objects.create(username=username,
                                   password='123456',
                                   nickname='王五')
        # profile = UserProfile.objects.create(user=user, username=username)
        profile = UserProfile.objects.create(user=user, usernamex=username)
        # 4. 反馈结果:成功/失败
        return HttpResponse('ok')
    except Exception as e:
        user.delete()
        print(e)
        return HttpResponse('no')


@transaction.atomic()
def user_signup_trans(request):
    """ 事务的使用-装饰器 """
    username = '13000000003'
    user = User.objects.create(username=username,
                               password='123456',
                               nickname='王五')
    profile = UserProfile.objects.create(user=user, usernamex=username)
    return HttpResponse('ok')


def user_signup_trans_with(request):
    """ 事务的使用-with语法"""
    with transaction.atomic():
        username = '13000000005'
        user = User.objects.create(username=username,
                                   password='123456',
                                   nickname='王五')
        profile = UserProfile.objects.create(user=user, usernamex=username)
    return HttpResponse('ok')


# @transaction.atomic()
def user_signup_trans_hand(request):
    """ 事务的自动提交 """
    username = '13000000007'
    # 放弃自动提交事务
    transaction.set_autocommit(False)
    try:
        user = User.objects.create(username=username,
                                   password='123456',
                                   nickname='王五')
        profile = UserProfile.objects.create(user=user, username=username)
        # profile = UserProfile.objects.create(user=user, usernamex=username)
        # 手动提交事务
        transaction.commit()
        # 4. 反馈结果:成功/失败
        return HttpResponse('ok')
    except Exception as e:
        # user.delete()
        print(e)
        # 手动控制事务，实现回滚
        transaction.rollback()
        return HttpResponse('no')


def user_login(request):
    """ 用户登录 """
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print('表单验证通过')
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'user_login.html', {
        'form': form
    })


def user_edit(request):
    """ 用户信息维护 """
    if request.method == 'POST':
        form = UserEditForm(data=request.POST)
        if form.is_valid():
            print('表单通过验证')
    else:
        form = UserEditForm()
    return render(request, 'user_edit.html', {
        'form': form
    })


def user_reg(request):
    """ 用户注册 """
    if request.method == 'POST':
        data = request.POST
        print('post data: ', data)
        # form = UserRegForm(data=request.POST, files=request.FILES)
        form = UserRegForm(request.POST, request.FILES)
        # 是否已经通过表单验证
        if form.is_valid():
            form_data = form.cleaned_data
            print('验证通过后的数据：', form_data)
        else:
            # 表单没有通过验证
            print(form.errors.as_json())
    else:
        # 表单初始化的数据
        initial_data = {
            'nickname': '默认昵称',
            'birth_date': '2000-1-1'
        }
        form = UserRegForm(initial=initial_data)
    return render(request, 'user_reg.html', {
        'form': form
    })


def user_change(request):
    """ 用户信息维护-基于ORM创建的表单 """
    if request.method == 'POST':
        form = UserChangeForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            print('表单通过验证')
            return redirect('/')
    else:
        form = UserChangeForm()
    return render(request, 'user_change.html', {
        'form': form
    })


def upload_use_form(request):
    """ 文件上传-表单上传 """
    if request.method == 'POST':
        file = request.FILES.get('avatar', None)
        if file:
            filename = os.path.join(settings.MEDIA_ROOT, 'test.jpg')
            with open(filename, 'wb+') as dest:
                for chunk in file.chunks():
                    dest.write(chunk)
            print('上传成功')
    return render(request, 'upload_use_form.html')


def upload_use_form2(request):
    """ 文件上传-表单上传 """
    if request.method == 'POST':
        form = AvatarUploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            file = form.cleaned_data['avatar']
            filename = os.path.join(settings.MEDIA_ROOT, 'avatar.jpg')
            with open(filename, 'wb+') as dest:
                for chunk in file.chunks():
                    dest.write(chunk)
            print('上传成功')
    else:
        form = AvatarUploadForm()
    return render(request, 'upload_use_form2.html', {
        'form': form
    })