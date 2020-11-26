from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
# Create your views here.

class Zhugeviews(APIView):

    def post(self,request,*args, **kwargs):
        #启动爬虫
        url = 'http://localhost:6800/schedule.json'
        project = request.data.get('project')
        spider = request.data.get('spider')
        if all([project,spider]):
            res = requests.post(url=url,data = {'project':project, 'spider':spider} )
            if res.status_code == 200 :
                return Response({'code':200,'status':'开始挖掘','spder':spider,
                    '停止蜘蛛':'curl http://localhost:6800/cancel.json -d project=scrapy -d job=运行ID',
                    'data': res.text})
        return Response({'code':404,'status':'为找到或者爬去失败'})

    def put(self,request,*args, **kwargs):
        '''停止爬虫'''
        url = 'http://localhost:6800/cancel.json'
        project = request.data.get('project')
        job = request.data.get('job')
        if all([project,job]):
            res = requests.post(url=url,data = {'project':project, 'job':job} )
            if res.status_code == 200 :
                return Response({'code':200,'status':'停止成功','data': res.text})
        return Response({'code':404,'status':'请输入需要停止的蜘蛛'})



