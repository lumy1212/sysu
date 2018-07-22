from django import forms
from .models import Function, Column, Post, Comment, ThumbUp


class FunctionForm(forms.ModelForm):
    class Meta:
        model = Function
        fields = ['text']
        labels = {'text': ''}


class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ['name']
        labels = {'name': '栏目名称'}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','text']
        labels = {'title': '标题','text':'正文'}
        widgets = {'title': forms.Textarea(attrs={'rows': 1}),'text': forms.Textarea(attrs={'cols': 80})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': '评论内容'}
