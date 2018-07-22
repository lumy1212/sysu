
from django.db import models
from django.contrib.auth.models import User


class Function(models.Model):
    """功能"""
    text = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '功能'
        ordering = ['text']     # 按名称排序

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Column(models.Model):
    """栏目"""
    # 所属功能
    function = models.ForeignKey(Function, on_delete=models.CASCADE, verbose_name='所属功能',default = "")
    # 栏目名称
    name = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

    class Meta:
        verbose_name_plural = '栏目'
        ordering = ['name']     #按名称排序


class Post(models.Model):
    """论坛帖"""
    column = models.ForeignKey(Column,on_delete=models.CASCADE, verbose_name='所属栏目')
    title = models.TextField('标题',max_length = 200)
    text = models.TextField('内容',default='',blank = True)
    date_added = models.DateTimeField('创建日期',auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')
    read_num = models.IntegerField('阅读量', default=0)

    class Meta:
        verbose_name_plural = '文章'

        def __str__(self):
            """返回模型的字符串表示"""
            return self.title[:50] + "..."

class Comment(models.Model):
    """评论,一条评论对一篇帖，一篇帖可有多条评论"""
    #评论文章
    post = models.ForeignKey(Post,on_delete = models.CASCADE,verbose_name = '所评文章')
    #评论者
    reviewer = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='评论者')
    #评论时间
    date = models.DateTimeField(auto_now_add=True)
    #评论内容
    text = models.TextField('内容', default='', blank=True)
    # 父评论，即所回复的评论
    parent_comment = models.ForeignKey("self", related_name='p_comment', blank=True, null=True,on_delete = models.CASCADE,default = None)
    #楼层
    floor = models.IntegerField('楼层')

    class Meta:
        verbose_name_plural = '评论'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."

class ThumbUp(models.Model):
    """点赞"""
    #所属文章
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='点赞文章')
    #点赞者
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='点赞者')
    #点赞时间
    time = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = '点赞'
