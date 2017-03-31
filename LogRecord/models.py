# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : sven_weng@wengyb.com
# Web   : http://wybblog.applinzi.com
from django.db import models


class Log(models.Model):
	username = models.CharField(max_length=100)
	nickname = models.CharField(max_length=100)
	operate_time = models.DateTimeField(auto_now_add=True)
	operate_action = models.CharField(max_length=100)