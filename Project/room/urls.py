from django.urls import path
from . import views

#loginrequiredmixedin
#post man bata data tanna milcha
app_name='room'
urlpatterns = [

		
		path('', views.home ,name='home'),
		path('about/', views.about ,name='about'),
		path('profile/',views.profile,name='profile'),
		path('profile/posting/',views.post_rent,name='post_rent'),
		
	]