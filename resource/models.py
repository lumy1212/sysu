from django.db import models
from django.contrib.auth.models import User

'''
def user_directory_path(instance, filename):
	return 'upload/data/user_{0}{1}.format(instance.user.id, filename)'
'''

class Topic(models.Model):
	text = models.CharField(max_length=30)
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.text
	
class MyFile(models.Model):
	filename = models.CharField('文件名',max_length=50)
	content = models.FileField('文件',upload_to='upload/data/')
	date_added = models.DateTimeField('上传时间',auto_now_add=True)
	uploader = models.ForeignKey(User, on_delete=True)
	topic = models.ForeignKey(Topic, on_delete=True)
	
	def __str__(self):
		return self.filename

		

