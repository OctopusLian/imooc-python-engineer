from django.urls import path

from grade import views

urlpatterns = [
    # 聚合及统计
    path('page/grade/', views.page_grade, name='page_grade'),
]