from django.conf.urls import patterns,url

from blog import views

urlpatterns=patterns('',
    url(r'^$',views.blogs,name="blogs"),
	url(r'^(?P<blog_id>\d+)/$',views.detail,name='detail'),
    url(r'^category/$',views.category,name='category'),
    url(r'^music/$',views.Music,name='music'),
    url(r'^timeline/$',views.Archive,name='timeline'),
)
