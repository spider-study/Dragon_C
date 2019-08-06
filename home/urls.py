from django.urls import path
from home import views
urlpatterns = [
    path('',views.index,name='homeindex'),
    path('upload/',views.upload),
    path('hehe/',views.hehe)
]