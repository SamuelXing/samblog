from haystack import indexes
from blog.models import Blog,Category

class BlogIndex(indexes.SearchIndex,indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	blog_name=indexes.CharField(model_attr='blogname')
	content=indexes.CharField(model_attr='content')
	summary=indexes.CharField(model_attr='summary')
	created_at = indexes.DateTimeField(model_attr='created_at')

	def get_model(self): 
		return Blog


class CategoryIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	cat_name=indexes.CharField(model_attr='catname')

	def get_model(self):
		return Category



