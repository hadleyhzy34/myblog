from django.contrib import admin
from .models import Article, Category
from django.db import models
from markdownx.admin import MarkdownxModelAdmin
# from markdown_editor.widgets import AdminMarkdownWidget

# Register your models here.

# admin.site.register(Article)
admin.site.register(Category)

class ProjectsAdmin(admin.ModelAdmin):
	pass

admin.site.register(Article, MarkdownxModelAdmin)