from django import forms
from .import models
from .models import Article, Category

choices = Category.objects.all().values_list('name','name')

choices_list =[]

for item in choices:
	choices_list.append(item)

class CreateArticle(forms.ModelForm):
	class Meta:
		model = models.Article
		fields=['title','slug','body','category', 'thumb','snippetbody', 'tags',]

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'slug': forms.TextInput(attrs={'class': 'form-control'}),
			'category':forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'snippetbody': forms.Textarea(attrs={'class': 'form-control'}),
		}