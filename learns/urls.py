from . import views
from django.urls import path


urlpatterns=[
    path('', views.index, name='stating_page'),
    path('posts', views.posts, name='post_page'),
    path('post/<slug:slug>/', views.single_post, name='post_detail'),
]