from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Blog

# Create your views here.
def blogs(request):
	latest_blog_list=Blog.objects.all().order_by('-created_at')[:5]
	context={'latest_blog_list':latest_blog_list}
	return render(request,'blog/index.html',context)
