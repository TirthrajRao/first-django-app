from django.urls import path

from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('post', views.post, name='post'),
    path('logout', views.logout, name='logout'),
    path('feedback', views.feedback, name='feedback'),
]