'''define urls in resource'''
app_name='resource'

from django.urls import path
'''
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
'''

from . import views

urlpatterns = [
	path('topics', views.topics, name='topics'),
	
	path('topics/(<topic_id>\d+)/', views.topic, name='topic'),
	
	path('download/(<file_id>\d+)/', views.download, name='download'),
		
	path('upload/', views.upload, name='upload'),
	
	path('upload/success/', views.upload_success, name='upload_success'),

	path('search/', views.search, name='search'),
	
	] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
