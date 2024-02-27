from django.urls import path
from . import views

urlpatterns = [
    path("",views.register,name="register"),
    path("log_in/",views.log_in,name="log_in"),
    path("log_out",views.log_out,name="log_out"),
    path("home/",views.home,name="home"),
    path("edit/<int:manage_id>/",views.edit,name="edit"),
    path("delete/<int:manage_id>/",views.delete,name="delete"),
]