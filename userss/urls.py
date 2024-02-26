from django.urls import path
from . import views


urlpatterns = [
    path("",views.home, name="home"),
    path("signin/",views.signin, name="signin"),
    path("signup/",views.signup, name="signup"),
    path("signout/",views.signout, name="signout"),
    path("blog/",views.blog, name="blog"),
    path('accounts/login/', views.signin, name='signin'),
    path('detail/<str:title>/', views.detail, name='detail'),
    path('user_blog_detail/', views.user_blog_detail, name='user_blog_detail'),
    path('user_blog_edit/<int:id>/', views.user_blog_edit, name='user_blog_edit'),
    path('user_blog_delete/<int:id>/', views.user_blog_delete, name='user_blog_delete'),
]

