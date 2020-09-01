from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from .import views

app_name = 'articles'

urlpatterns = [
	path('', views.article_list, name="list"),
	path('create/', views.article_create, name="create"),
	path('<slug:slug>/', views.article_details, name="detail"),
	path('tag/<slug:slug>/', views.article_tagged, name="tagged"),
	path('category/<str:category>', views.article_category, name="category"),
]