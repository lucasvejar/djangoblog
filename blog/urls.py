from django.urls import path
from . import views

app_name= 'blog'
urlpatterns = [
    path(r'', views.post_list, name='post_list'),
    path('login/',views.loginPage, name='login'),
    path('register/',views.registerUser,name='register'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]