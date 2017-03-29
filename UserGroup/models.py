from django.db import models


# Create your models here.
class UserGroup(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=100)
	level = models.IntegerField()
	nickname = models.CharField(max_length=10)
	login_token = models.CharField(max_length=100, blank=True)
	last_login_time = models.DateField(auto_now=True)
	create_time = models.DateTimeField(auto_now_add=True)
