'''define forms in resource'''

from django import forms
from .models import MyFile, Topic

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']

class MyFileForm(forms.ModelForm):
	class Meta:
		model = MyFile
		fields = ['filename','content','topic']
		labels = {'filename':'文件名','content':'文件','topic':'所属分类'}
