from django.shortcuts import render
from django.urls import reverse
from django.http import StreamingHttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import MyFile, Topic
from .forms import MyFileForm, TopicForm

def index(request):
	return(request, 'resource/index.html')
	
def topics(request):
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'resource/topics.html', context)

def topic(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	myfiles = topic.myfile_set.order_by('-date_added')
	context = {'topic': topic, 'myfiles': myfiles}
	return render(request, 'resource/topic.html', context)

@login_required
def download(request, file_id):
	myfile = MyFile.objects.get(id=file_id)
	the_file_name = myfile.filename
	file_path = 'upload/data/' + the_file_name 

	def read_file(filename, chunk_size=512):
		with open(filename, 'rb') as f:
			while True:
				c = f.read(chunk_size)
				if c:
					yield c
				else:
					break
				
	response = StreamingHttpResponse(read_file(file_path))
	
	response['Content-Type'] = 'application/octet-stream'
	response['Content-Disposition'] = 'attachment; filename=%s' %myfile.filename
		
	return response
	

@login_required
def upload(request):	
	if request.method == 'POST':	
		form = MyFileForm(request.POST,request.FILES)
		if form.is_valid():
			new_file = form.save(commit=False)
			new_file.uploader = request.user
			new_file.save()
			return HttpResponseRedirect(reverse('resource:upload_success'))
	else:
		form = MyFileForm()
	return render(request, 'resource/upload.html', {'form':form})

def upload_success(request):
	return render(request, 'resource/upload_success.html')
	
def search(request):
	if request.method == 'GET':
		file_name = request.GET.get('search')
		try:
		    results = MyFile.objects.filter(filename__icontains=file_name)
		except MyFile.DoesNotExist:
			results = None
		return render(request, 'resource/search.html', {'myfiles': results})
	else:
	    return render(request, 'resource/search.html', {})