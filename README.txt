运行环境：进入项目文件ducks，虚拟环境运行
目录下sysly为总项目文件夹
目前实际使用到的应用程序包括app1文件夹、users文件夹、resource文件夹
其中app1涉及与功能、栏目、帖子等有关的功能以及主界面
users包含用户注册、登录、登出、以及用户个人信息等相关功能
resource包括文件上传下载搜索等功能，资源的根目录是‘/upload’文件夹
static文件夹中包含静态页面图片
-------------------------------------------------------------------------
已实现功能：用户注册、登录，查看栏目、文章，搜索、创建、编辑文章，评论，回复，搜索资料，资料上传下载，个人信息查看及修改
-------------------------------------------------------------------------
后台管理：
超级用户1：用户名 ：txq，密码：123qweasd，
超级用户2：用户名Lily， 密码YeXiu0529

栏目创建权限仅归超级用户所有，可添加、编辑栏目
-------------------------------------------------------------------------
修改路径：
sysly/setting.py最后面，MEDIA_ROOT与STATICFILES_DIRS需修改为本地路径
MEDIA_ROOT = r'项目路径'
STATICFILES_DIRS = [r'项目路径\static']
例如：
MEDIA_ROOT = r'C:\Users\80703\Desktop\ducks\ducks'
STATICFILES_DIRS = [r'C:\Users\80703\Desktop\ducks\ducks\static']
