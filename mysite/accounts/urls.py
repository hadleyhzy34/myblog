from django.conf.urls import url
from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [
	url('signup/',views.signup_view, name="signup"),
	url('login/', views.login_view, name="login"),
	url('logout/', views.logout_view, name="logout"),
]