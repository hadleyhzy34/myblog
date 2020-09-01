from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article, Category
from taggit.models import Tag

def home(request):
	categories = Category.objects.all()
	articles = Article.objects.all().order_by('-date')
	# return HttpResponse('homepage')
	# common_tags = articles.tags.most_common()[:20]
	tags = Tag.objects.all()
	context = {
		'articles':articles,
		'categories':categories,
		'tags':tags
		# 'common_tags':common_tags,
	}
	return render(request,'homepage.html',context);


def about(request):
	# return HttpResponse('about')
	return render(request,'about.html');