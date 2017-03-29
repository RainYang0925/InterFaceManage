# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : sven_weng@wengyb.com
# Web   : http://wybblog.applinzi.com

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^user/', views.user, name='user'),
	url(r'^usercenter/', views.usercenter, name='usercenter'),
	url(r'^operationlog/', views.operation_log, name='operationlog'),
	url(r'^updateinfo/', views.update_info, name='updateinfo'),

	# ================================Ajax=================================
	url(r'^checktoken/$', views.check_token),
	url(r'^checkauth/$', views.check_auth),
	url(r'^signout/$', views.sign_out),
]
