from django.urls import path
from . import views

app_name= 'blog'
urlpatterns = [
    path(r'', views.loginPage, name='login'),
    path('login/',views.loginPage, name='login'),
    path('home/',views.home, name='home'),
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.registerUser,name='register'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/inbox',views.inbox, name='inbox'),
    path('post/trendingTopics', views.trendingTopics, name='trendingTopics'),
    path('post/profile',views.profile, name='profile'),
    path('post/<int:pk>/makeComment',views.makeComment, name='makeComment'),
]