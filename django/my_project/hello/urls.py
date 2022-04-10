from django.urls import path

from hello.views import index

urlpatterns = [
    path('index/', index, name='index'),
]