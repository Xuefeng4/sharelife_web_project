from django.conf.urls import url,include
from django.urls import path

from . import views

app_name = 'shareLife'
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('form', views.form, name='form'),
    path('post/<int:pk>', views.detail, name = "post_detail"),
   #path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('post/<int:pk>/update/', views.updatePost.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.deletePost.as_view(), name='post_delete'),
    path('index/search',views.search, name='search')
]
    #detail page

