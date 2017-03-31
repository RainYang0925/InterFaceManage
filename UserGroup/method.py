# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : sven_weng@wengyb.com
# Web   : http://wybblog.applinzi.com


import os
import django
import hashlib
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestTool.settings')
django.setup()
from UserGroup.models import UserGroup


class Login(object):
	"""登录相关"""
	def login_check(self, username, password):
		"""
		登录校验
		:param username: {str} 用户名
		:param password: {str} 密码
		:return: {boolen} True/False
		"""
		try:
			usergroup = UserGroup.objects.get(username=username)
		except Exception:
			return False
		return True if usergroup.password == password else False

	def check_token(self, token):
		"""
		校验token
		:param token: {str} 用户的token
		:return: {boolen} True/False
		"""
		try:
			UserGroup.objects.get(login_token=token)
			return True
		except Exception:
			return False

	def check_auth(self, token, need_auth):
		"""
		鉴权
		:param token: {str} 用户token
		:param need_auth: {str} 鉴权等级
		:return: {boolen} True/False
		"""
		try:
			usergroup = UserGroup.objects.get(login_token=token)
			return True if usergroup.level == need_auth else False
		except Exception:
			return False

	def write_hash(self, username):
		"""
		写入Token
		:param username: {str} 用户名
		:return: {boolen} True/False
		"""
		m = hashlib.md5()
		m.update('wengyb' + time.ctime())
		hash_result = m.hexdigest()
		print hash_result
		try:
			is_write = UserGroup.objects.get(username=username)
			is_write.login_token = hash_result
			is_write.save()
			return True
		except Exception:
			return False

	def get_user_info(self, para_key, type):
		"""
		获取用户信息,调用之前确保使用login_check校验通过
		:param para_key: {str} 查询条件的值
		:return: {dick} params={'nickname', 'loginToken'}
		"""
		if type == 'username':
			userinfo = UserGroup.objects.get(username=para_key)
		elif type == 'token':
			userinfo = UserGroup.objects.get(login_token=para_key)
		data = {
			'nickname': userinfo.nickname,
			'loginToken': userinfo.login_token,
			'username': userinfo.username,
			'level': userinfo.level
		}
		return data

	def sign_out(self, token):
		"""
		用户登出
		:param token:{str} 登录的token
		:return: {boolen} True/False
		"""
		try:
			userinfo = UserGroup.objects.get(login_token=token)
		except Exception:
			return False
		userinfo.login_token = ''
		userinfo.save()
		return True


class UserInfo(object):
	def check_password(self, token, pwd):
		"""
		校验用户密码是否正确
		:param pwd: {str} 密码
		:return: {boolen} True/False
		"""
		try:
			userinfo = UserGroup.objects.get(login_token=token)
		except Exception:
			return False
		return True if userinfo.password == pwd else False

	def update_password(self, username, pwd):
		"""
		修改密码
		:param username:{str} 用户名
		:param pwd:{str} 密码
		:return:{boolen} True/False
		"""
		try:
			userinfo = UserGroup.objects.get(username=username)
			userinfo.password = pwd
			userinfo.save()
			return True
		except Exception:
			return False



if __name__ == '__main__':
	login = Login()
	# print login.login_check('wengyb', '111222')
	# login.write_hash('wengyb')
	print login.check_auth('9e68f222320ca564e780b82fe5f9e271', 1)