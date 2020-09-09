from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Article, Category
from django.contrib.auth.decorators import login_required
from .import forms
from django.views.generic import TemplateView
from taggit.models import Tag


# Create your views here.
def article_list(request):
	articles = Article.objects.all().order_by('-date')
	categories = Category.objects.all()
	# common_tags = articles.tags.most_common()[:20]

	context = {
		'articles':articles,
		'categories':categories,
		# 'common_tags':common_tags,
	}
	return render(request, 'articles/article_list.html',context)

def article_details(request, slug):
	# return HttpResponse(slug)
	article = Article.objects.get(slug=slug)
	categories = Category.objects.all()
	# common_tags = article.tags.most_common()[:20]
	context = {
		'article':article,
		'categories':categories,
	}
	return render(request, 'articles/article_detail.html',context)

# @login_required(login_url="/accounts/login/")
# def article_create(request):
# 	if request.method =='POST':
# 		form = forms.CreateArticle(request.POST, request.FILES)
# 		if form.is_valid():
# 			#save article to db
# 			instance = form.save(commit=False)
# 			instance.author = request.user
# 			instance.save()
# 			return redirect('articles:list')
# 	else:
# 		form = forms.CreateArticle()
# 	return render(request, 'articles/article_create.html', {'form':form })

@login_required(login_url="/accounts/login/")
def article_create(request):
	common_tags = Article.tags.most_common()[:4]
	if request.method =='POST':
		form = forms.CreateArticle(request.POST, request.FILES)
		if form.is_valid():
			#save article to db
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			form.save_m2m()
			return redirect('articles:list')
	else:
		form = forms.CreateArticle()
	return render(request, 'articles/article_create.html', {'form':form })

# class MarkDown(TemplateView):
#     template_name = 'articles/article_detail.html'

#     def get_context_data(self, **kwargs):
#         markdowntext = open(os.path.join(os.path.dirname(__file__), 'templates/articles/test.md')).read()

#         context = super(MarkDown, self).get_context_data(**kwargs)
#         context['markdowntext'] = markdowntext

#         return context

# show articles based on tags
def article_tagged(request, slug):
	# tag = get_object_or_404(Tag, slug=slug)
	#filter posts by tag name
	# articles = Article.objects.filter(tags=tag)
	tags = Tag.objects.filter(slug=slug).values_list('name',flat=True)
	articles = Article.objects.filter(tags__name__in=[tags]).order_by('-date')
	categories = Category.objects.all()

	context = {
		'articles':articles,
		'categories':categories,
	}
	return render(request, 'articles/article_list.html',context)

# show articles based on category
def article_category(request, category):
	articles = Article.objects.filter(category=category).order_by('-date')
	categories = Category.objects.all()

	context = {
		'articles':articles,
		'categories':categories,
	}
	return render(request, 'articles/article_list.html',context)