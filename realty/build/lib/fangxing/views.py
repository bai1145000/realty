from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
# Create your views here.

class FangxingErshouviews(APIView):

    def post(self,request,*args, **kwargs):
        #启动爬虫
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'ABCkg', 'spider': 'abckg'}
        return JsonResponse({'result':'ok'})

