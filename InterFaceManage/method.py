# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : sven_weng@wengyb.com
# Web   : http://wybblog.applinzi.com
import os
import django
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestTool.settings')
django.setup()

from InterFaceManage.models import Interface


class ApiManage(object):
	def create_api(self, api_info):
		isWrite = Interface(ApiStatus=api_info['api_status'],
							BelongModel=api_info['belong_model'],
							BelongSystem=api_info['belong_system'],
							RequestMethod=api_info['request_method'],
							MockUrl=api_info['mock_url'],
							RequestHeadDoc=api_info['request_head_doc'],
							ApiName=api_info['api_name'],
							UserRange=api_info['user_range'],
							ApiUrl=api_info['api_url'],
							RightReturnDoc=api_info['right_return_doc'],
							ErrReturnDoc=api_info['err_return_doc'],
							ErrCode=api_info['err_code'],
							ApiVersion=api_info['api_version'],
							Developer=api_info['developer'],
							RequestDemo=api_info['request_demo'],
							InputParas=api_info['input_paras'],
							ReturnParas=api_info['return_paras'])
		isWrite.save()

	def update_api(self, api_id, api_info):
		obj = Interface.objects.get(id=api_id)
		obj.ApiStatus = api_info['api_status']
		obj.BelongModel = api_info['belong_model']
		obj.BelongSystem = api_info['belong_system']
		obj.RequestMethod = api_info['request_method']
		obj.MockUrl = api_info['mock_url']
		obj.RequestHeadDoc = api_info['request_head_doc']
		obj.ApiName = api_info['api_name']
		obj.UserRange = api_info['user_range']
		obj.ApiUrl = api_info['api_url']
		obj.RightReturnDoc = api_info['right_return_doc']
		obj.ErrReturnDoc = api_info['err_return_doc']
		obj.ErrCode = api_info['err_code']
		obj.ApiVersion = api_info['api_version']
		obj.Developer = api_info['developer']
		obj.RequestDemo = api_info['request_demo']
		obj.InputParas = api_info['input_paras']
		obj.ReturnParas = api_info['return_paras']
		obj.save()