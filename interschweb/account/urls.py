from django.urls import path, include
from . import views

app_name = 'account'
urlpatterns = [
	path('login/', views.signin, name='login'),
	path('signup/', views.signup, name='signup'),
]