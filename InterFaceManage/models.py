from django.db import models


class Interface(models.Model):
	ApiStatus = models.CharField(max_length=5)
	BelongModel = models.CharField(max_length=20)
	BelongSystem = models.CharField(max_length=20)
	RequestMethod = models.CharField(max_length=10)
	MockUrl = models.CharField(max_length=100)
	RequestHeadDoc = models.CharField(max_length=500)
	ApiName = models.CharField(max_length=20)
	UserRange = models.CharField(max_length=500)
	ApiUrl = models.CharField(max_length=100)
	RightReturnDoc = models.CharField(max_length=500)
	ErrReturnDoc = models.CharField(max_length=500)
	ErrCode = models.CharField(max_length=500)
	ApiVersion = models.CharField(max_length=10)
	Developer = models.CharField(max_length=10)
	RequestDemo = models.CharField(max_length=500)
	InputParas = models.CharField(max_length=2000)
	ReturnParas = models.CharField(max_length=2000)
	CreateData = models.DateTimeField(auto_now_add=True)
	UpdateData = models.DateTimeField(auto_now=True)