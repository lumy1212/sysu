"""定义app1的URL模式"""
from django.conf.urls import url
from . import views
app_name = 'app1'

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    # 讨论区
    url(r'^discuss/$', views.discuss, name='discuss'),
    # 资源库
    url(r'^resource/topics/$', views.resource, name='resource'),
    # 资源库
    url(r'^entertainment/$', views.entertainment, name='entertainment'),
    # 显示所有的栏目
    url(r'^columns/$', views.columns, name='columns'),
    # 特定栏目的详细页面
    url(r'^column/(?P<column_id>\d+)/$', views.column, name='column'),
    # 用于添加新主题的网页,
    url(r'^new_column/$', views.new_column, name='new_column'),
    # 用于添加新帖的页面
    url(r'^new_post/(?P<column_id>\d+)/$', views.new_post, name='new_post'),
    # 用于编辑帖子的页面
    url(r'^edit_post/(?P<post_id>\d+)/$', views.edit_post,name='edit_post'),
    # 特定文章的详细页面
    url(r'^view_post/(?P<post_id>\d+)/$', views.view_post, name='view_post'),
    # 用于添加评论
    url(r'^view_post/(?P<post_id>\d+)/$', views.view_post, name='new_comment'),
    #用于点赞
    url(r'^view_post/(?P<post_id>\d+)/$', views.view_post, name='thumb_up'),
    # 用于回复评论
    url(r'^view_post/(?P<post_id>\d+)/$', views.view_post, name='reply'),
    # 搜索讨论区帖
    url(r'^search_post/$', views.search_post, name='search_post'),
    # 搜索休闲区帖
    url(r'^search_post/$', views.search_entertain_post, name='search_entertain_post'),
]