from django.contrib import admin
from blog.models import Blog
from blog.models import Category
# from blog.models import blog_with_cat

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display=('name','created_at')
	list_filter=['created_at']
	search_fields=['name']
	date_hierarchy = 'created_at'

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)
# admin.site.register(blog_with_cat)