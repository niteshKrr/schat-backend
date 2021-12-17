from django.contrib import admin
from django.urls import path , include
from schat import views

urlpatterns = [
    # path('', views.index , name='home'),
    path('user', views.user , name='user'),
    path('user/<int:pk>', views.user1 , name='user1'),
    path('msg', views.msg , name='msg'),
    path('msg/<int:pk>', views.msg1 , name='msg1')

]