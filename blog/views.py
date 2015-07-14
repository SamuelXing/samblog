from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import markdown2

from blog.models import Blog
from blog.models import Category

# Create your views here.
def blogs(request):
	latest_blog_list=Blog.objects.all().order_by('-created_at')[:5]
	for blog in latest_blog_list:
		blog.html_content=markdown2.markdown(blog.content)
	context={'latest_blog_list':latest_blog_list}
	return render(request,'index.html',context)

def detail(request,blog_id):
	blog=get_object_or_404(Blog,pk=blog_id)
	blog.html_content=markdown2.markdown(blog.content)
	return render(request,'detail.html',{'blog':blog})

def category(request):
	cat_list=Category.objects.all().order_by('number')
	blog_list=Blog.objects.all()
	for cat in cat_list:
		for blog in blog_list:
			if cat.id == blog.cat_name.id:
				cat.number=cat.number+1

	context={'category_list':cat_list, \
	         'blog_list':blog_list}
	return render(request,'category.html',context)

def Music(request):
	return render(request,'music.html')

def Archive(request):
	blog_list=Blog.objects.all().order_by('-created_at')
	month_list=[]
	year_list=[]
	for blog in blog_list:
		month_list.append(blog.created_at.strftime('%b'))
		year_list.append(blog.created_at.strftime('%Y'))

	month_list=list(set(month_list))
	year_list=list(set(year_list))

	context={'blog_list':blog_list,\
	         'year_list':year_list,\
	         'month_list':month_list,\
	         }
	return render(request,'timeline.html',context)