from django.urls import path
from . import views

urlpatterns=[
    path('',views.login , name='login'),
    path('registration',views.registration , name='regis'),
    path('home',views.home, name='home'),
    path('login_btn',views.login_btn),
    path('register',views.register)



]