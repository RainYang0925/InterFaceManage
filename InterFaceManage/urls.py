# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : sven_weng@wengyb.com
# Web   : http://wybblog.applinzi.com

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='interfacemanageindex'),
	url(r'^newinterface/', views.newinterface, name='newinterface'),
	url(r'^interface/(?P<api_id>\d+)/$', views.interface),
	url(r'^updateapi/(?P<api_id>\d+)/$', views.update_api, name='updateapi'),
	url(r'^qryapi/', views.qry_api, name='qryapi'),
	# ============Ajax==============
	url(r'^getapirecord/', views.get_api_record),
	url(r'^getapi/', views.get_api),
 ]