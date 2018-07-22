from django.contrib import admin

from app1.models import Column,Function,Post,Comment,ThumbUp

class FunctionAdmin(admin.ModelAdmin):
    Function.objects.order_by("text")
    list_display = ('id','text')

class ColumnAdmin(admin.ModelAdmin):
    Column.objects.order_by("name")
    list_display = ('id','function','name')


class PostAdmin(admin.ModelAdmin):
    Column.objects.order_by('id')
    list_display = ('id','column','title','author','date_added')

class CommentAdmin(admin.ModelAdmin):
    Comment.objects.order_by('id')
    list_display = ('id','post','reviewer','date','text','parent_comment','floor')


admin.site.register(Column,ColumnAdmin)
admin.site.register(Function,FunctionAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(ThumbUp)
