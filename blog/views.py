from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import markdown2

from blog.models import Blog


# Create your views here.
def blogs(request):
	latest_blog_list=Blog.objects.all().order_by('-created_at')[:5]
	context={'latest_blog_list':latest_blog_list}
	return render(request,'index.html',context)

def detail(request,blog_id):
	blog=get_object_or_404(Blog,pk=blog_id)
	blog.html_content=markdown2.markdown(blog.content)
	return render(request,'detail.html',{'blog':blog})
