# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : sven_weng@wengyb.com
# Web   : http://wybblog.applinzi.com
from django.shortcuts import render


def index(request):
	return render(request, 'InterFaceManage/index.html')