from django.contrib import admin
from blog.models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display=('name','created_at')
	list_filter=['created_at']
	search_fields=['name']
	date_hierarchy = 'created_at'

admin.site.register(Blog,BlogAdmin)
