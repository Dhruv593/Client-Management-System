from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('login', views.login, name= 'login'),
    path('dashboard', views.dashboard, name= "dashboard"),
    path('logout', views.logout, name="logout"),
    path('create-record', views.create_record, name="create-record"),
    path('record/<int:pk>', views.record, name="record"),
    path('update-record/<int:pk>', views.update_record, name='update-record'),
    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),

]