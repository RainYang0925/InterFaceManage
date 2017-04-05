# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : sven_weng@wengyb.com
# Web   : http://wybblog.applinzi.com

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestTool.settings')
django.setup()
from LogRecord.models import Log


class LogOperate(object):

	def write_log(self, record):
		try:
			username = record['username']
			nickname = record['nickname']
			operate_action = record['operate_action']
			isWrite = Log(username=username,
						  nickname=nickname,
						  operate_action=operate_action)
			isWrite.save()
		except Exception as e:
			print e
