from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from taggit.managers import TaggableManager

# Create your models here.
# convention to create new class upper case

class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name


class Article(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	# body = models.TextField(default='this is test')
	# body = RichTextField(blank=True, null=True)
	body = MarkdownxField()
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.png',blank=True)
	category = models.CharField(max_length=255, default='coding')
	snippetbody = RichTextField(blank=True, null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	tags = TaggableManager()
	#add in thmbnail later

	#add in author later


	def __str__(self):
		return self.title

	@property
	def formatted_markdown(self):
		return markdownify(self.body)
	

	def snippet(self):
		return self.body[:100]
		# return self.body[:50] + '...'