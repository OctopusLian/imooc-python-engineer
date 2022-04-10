from django.urls import path

from accounts import views

urlpatterns = [
    path('user/info/', views.user_info, name='user_info'),
    path('user/list/slice/', views.user_list_slice, name='user_list_slice'),
    path('user/list/paginator/', views.user_list_paginator, name='user_list_paginator'),
    path('user/list/class/', views.UserListView.as_view(), name='user_list_class'),
    path('user/register/', views.user_register, name='user_register'),
    path('user/signup/trans/', views.user_signup_trans, name='user_signup_trans'),
    path('user/signup/with/', views.user_signup_trans_with, name='user_signup_trans_with'),
    path('user/signup/hand/', views.user_signup_trans_hand, name='user_signup_trans_hand'),
    # 用户登录表单
    path('user/login/', views.user_login, name='user_login'),
    # 用户信息维护
    path('user/edit/', views.user_edit, name='user_edit'),
    # 用户注册
    path('user/reg/', views.user_reg, name='user_reg'),
    # 用户信息维护-ORM表单
    path('user/change/', views.user_change, name='user_change'),
    # 表单文件上传
    path('upload/form/', views.upload_use_form, name='upload_use_form'),
    path('upload/form2/', views.upload_use_form2, name='upload_use_form2'),
]