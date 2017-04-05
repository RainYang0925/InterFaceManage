# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : sven_weng@wengyb.com
# Web   : http://wybblog.applinzi.com
from django.http import JsonResponse
from django.shortcuts import render
from .models import Log
from UserGroup.method import Login

login = Login()


def get_log(request):
	token = request.GET.get('token')
	userinfo = login.get_user_info(token, 'token')
	username = userinfo['username']
	if userinfo['level'] == 99:
		userlog = Log.objects.all().order_by('-pk')[:50]
	else:
		userlog = Log.objects.filter(username=username).order_by('-pk')[:50]
	rst = []
	for x in userlog:
		data = x.nickname + '(' + x.username + u') 于 ' + str(x.operate_time) + u' 进行了 ' + x.operate_action + u' 操作'
		rst.append(data)
	return JsonResponse(rst, safe=False)


def write_log(request):
	pass


def get_api_log(request):
	api_log = Log.objects.filter(operate_action=u'新增接口').order_by('-pk')[:20]
	rst = []
	for x in api_log:
		data = x.nickname + '(' + x.username + u') 于 ' + str(x.operate_time) + u' 进行了 ' + x.operate_action + u' 操作'
		rst.append(data)
	return JsonResponse(rst, safe=False)