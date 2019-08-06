from  jianli import jianli_views
from django.urls import path
urlpatterns = [
    path('index', jianli_views.index,name='jianli_index'),
    path('about', jianli_views.about,name='about'),
    path('blog_post', jianli_views.blog_post,name='blog_post'),
    path('work_list', jianli_views.work_list,name='list'),
    path('work_his', jianli_views.work_his,name='history'),
    path('filename',jianli_views.file_down,name='down'),
]