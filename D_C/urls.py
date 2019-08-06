from django.urls import path

from D_C import views
urlpatterns = [
    path('',views.index),
]