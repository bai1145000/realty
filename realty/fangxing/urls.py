from django.contrib import admin
from django.urls import path,include
from .views import FangxingErshouviews
app_name = 'fangxing'

urlpatterns = [
    path('spider/', FangxingErshouviews.as_view()), #二手房
   
]