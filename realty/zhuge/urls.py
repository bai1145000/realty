from django.contrib import admin
from django.urls import path,include
from .views import Zhugeviews
app_name = 'zhuge'

urlpatterns = [
    path('spider/', Zhugeviews.as_view()), #二手房
   
]