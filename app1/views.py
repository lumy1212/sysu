from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

import time

from .models import Function, Column, Post, Comment, ThumbUp
from .forms import FunctionForm, ColumnForm, PostForm, CommentForm


def index(request):
    """主页"""
    return render(request, 'app1/index.html')

@login_required
def columns(request):
    """显示所有的栏目"""
    columns = Column.objects.order_by('name')
    context = {'columns': columns}
    return render(request, 'app1/columns.html', context)

@login_required
def discuss(request):
    """讨论区"""
    discuss = Function.objects.get(text="讨论区")
    columns = discuss.column_set.order_by('name')
    context = {'discuss': discuss, 'columns': columns}
    return render(request,'app1/DiscussColumn.html',context)

@login_required
def resource(request):
    """资源库"""
    resource = Function.objects.get(text="资源库")
    columns = resource.column_set.order_by('name')
    context = {'resource': resource, 'columns': columns}
    return render(request, 'resource/topics.html', context)


@login_required
def entertainment(request):
    """休闲区"""
    entertainment = Function.objects.get(text="休闲区")
    columns = entertainment.column_set.order_by('name')
    context = {'entertainment': entertainment, 'columns': columns}
    return render(request, 'app1/EntertainmentColumn.html', context)


@login_required
def column(request, column_id):
    """显示单个栏目及其所有的条目"""
    column = Column.objects.get(id=column_id)
    posts = column.post_set.order_by('-read_num')
    context = {'column': column, 'posts': posts}
    return render(request, 'app1/column.html',context)

@login_required
def new_column(request):
    """添加新栏目"""
    if request.method != 'POST':
        # 未提交数据： 创建一个新表单
        form = ColumnForm()
    else:
        # POST提交的数据,对数据进行处理
        form = ColumnForm(request.POST)
        if form.is_valid():
            new_column = form.save(commit=False)
            new_column.save()
            return HttpResponseRedirect(reverse('app1:columns'))

    context = {'form': form}
    return render(request, 'app1/new_topic.html', context)


@login_required
def new_post(request, column_id):
    """在特定的栏目中建新帖"""
    column = Column.objects.get(id=column_id)
    if request.method != 'POST':
        # 未提交数据,创建一个空表单
        form = PostForm()
    else:
        # POST提交的数据,对数据进行处理
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.column = column
            new_post.author = request.user
            new_post.date_added = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
            new_post.save()
            return HttpResponseRedirect(reverse('app1:column',args=[column_id]))

    context = {'column': column, 'form': form}
    return render(request, 'app1/new_post.html', context)


@login_required
def edit_post(request, post_id):
    """编辑既有条目"""
    post = Post.objects.get(id=post_id)
    column = post.column

    #需作者编辑
    if post.author != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求， 使用当前条目填充表单
        form = PostForm(instance=post)
    else:
        # POST提交的数据， 对数据进行处理
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app1:view_post',args=[post.id]))
    context = {'post': post, 'column': column, 'form': form}
    return render(request, 'app1/edit_post.html', context)


@login_required
def view_post(request, post_id):
    """显示帖子具体内容"""
    post = Post.objects.get(id=post_id)
    if not request.COOKIES.get('post_%s_readed' % post_id):
        post.read_num += 1
        post.save()
    comments = post.comment_set.order_by('date')
    thumbups = len(post.thumbup_set.order_by('user'))
    reply = 0
    parent_floor = 0

    # 未提交数据： 创建一个新表单
    form = CommentForm()
    if request.method == 'POST':
        if 'reply' in request.POST:
            # 回复评论
            reply = int(request.POST.get('reply'))
            parent_floor = Comment.objects.get(id=reply).floor
        elif 'submit' in request.POST:
            """添加新评论"""
            # POST提交的数据,对数据进行处理
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.reviewer = request.user
                new_comment.post = post
                new_comment.floor = len(post.comment_set.order_by('date'))+1
                reply = int(request.POST.get('submit'))
                if reply != 0:
                    new_comment.parent_comment = Comment.objects.get(id=reply)
                new_comment.save()
                return HttpResponseRedirect(reverse('app1:view_post', args=[post_id]))
        elif 'thumbup' in request.POST:
            """点赞"""
            new_thumbup = ThumbUp()
            new_thumbup.post = post
            new_thumbup.user = request.user
            new_thumbup.save()
            return HttpResponseRedirect(reverse('app1:view_post', args=[post_id]))
    context = {'comments':comments,'post': post,'form': form, 'thumbups':thumbups,
               'reply': reply, 'pf': parent_floor}
    response = render(request,'app1/view_post.html',context)
    response.set_cookie('post_%s_readed'% post_id,'true')
    return response


def search_post(request):
    if request.method == 'GET':
        title_ = request.GET.get('search')
        results = Post.objects.filter(title__icontains=title_)
        results_list = list(results)
        for post in results_list:
            if post.column.function.text != "讨论区":
                results_list.remove(post)
            return render(request, 'app1/search_post.html', {'posts': results_list})
        else:
            return render(request, 'app1/search_post.html', {})


def search_entertain_post(request):
    if request.method == 'GET':
        title_ = request.GET.get('search')
        results = Post.objects.filter(title__icontains=title_)
        results_list = list(results)
        for post in results_list:
            if post.column.function.text != "休闲区":
                results_list.remove(post)
            return render(request, 'app1/search_post.html', {'posts': results_list})
        else:
            return render(request, 'app1/search_post.html', {})
