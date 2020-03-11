from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('addition.html', views.addition, name="add"),
    path('subtraction.html', views.subtraction, name="sub"),
    path('multiplication.html', views.multiplications, name="multi"),
    path('division.html', views.division, name="division"),
]