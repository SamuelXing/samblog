from django.conf.urls import patterns,url

from blog import views

urlpatterns=patterns('',
	url(r'^$',views.blogs,name="blogs"),
	url(r'^(?P<blog_id>\d+)/$',views.detail,name='detail'),
)
