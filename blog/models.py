#-*- coding:utf-8 -*-

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import time,uuid
from django.utils import timezone

from samblog import settings

class Category(models.Model):
	name=models.CharField(max_length=50,verbose_name=u'名称')
	number=models.IntegerField(default=0,verbose_name=u'文章数')

	def __unicode__(self):
		return self.name

	class Meta:
		ordering=['-number']
		verbose_name_plural=verbose_name=u"分类"

# Create your models here.
class Blog(models.Model):
	user_name=models.ForeignKey(User,null=False,verbose_name=u'作者')
	cat_name=models.ForeignKey(Category,null=True,default='',verbose_name=u'分类 ')
	name=models.CharField(max_length=50,null=False,verbose_name=u'标题')
	summary=models.CharField(max_length=200,null=False,verbose_name=u'摘要')
	content=models.TextField(null=False,verbose_name=u'正文')
	created_at=models.DateTimeField(u'创建时间',auto_now_add=True)

	def __unicode__(self):
		return self.name
	'''
	def was_published_recently(self):
		return self.created_at>=timezone.now()-datetime.timedelta(days=1)
	was_published_recently.admin_order_field='created_at'
	was_published_recently.boolean=True
	was_published_recently.short_description=u'最近创建？'
	'''
	class Meta:
		ordering=['-created_at']
		verbose_name_plural=verbose_name=u"文章"

# class blog_with_cat(models.Model):
# 	blog=models.ForeignKey(Blog,null=False,verbose_name=u'文章')
# 	cat=models.ForeignKey(Category,null=False,verbose_name=u'分类')
#
# 	def __unicode__(self):
# 		return self.blog.name
#
# 	class Meta:
# 		verbose_name_plural=verbose_name=u"分类文章"