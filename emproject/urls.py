
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("home/", views.homePage, name="home"),
    path("add/", views.create_emp, name="adduser"),
    path("success/", views.successPage, name="success"),
    path("getall/", views.getAllUser, name="getallurl"),
    path("delete/<int:id>/", views.delete, name="user_delete"),
    path("update/<int:id>/", views.update_emp, name="user_update"),
]
