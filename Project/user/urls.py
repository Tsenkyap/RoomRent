from django.urls import path
from .import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


app_name='user'

urlpatterns = [

path('home/',views.home_view,name='home'),
	path('register/',views.register_view,name='register'),
		path('profile/',views.profile,name='profile'),
			path('profile/<int:pk>/',views.profile,name='profile_with_pk'),
				# path('connect/<str:operation>/<int:pk>/',views.change_friend,name='change_friend'),
						path('login/',views.login_view,name='login'),
							path('logout/',views.logout_view,name='logout'),	
									path('password-update/',views.password_change_view,name='password-change'),
										path('password-reset/',PasswordResetView.as_view(template_name='user/password_reset.html',email_template_name='user/reset_password_email.html',success_url= '/users/password-reset/done/'),name='password_reset'),
											path('password-reset/done/',PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
												path('password-reset/confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html',success_url='/users/password-reset/complete/'),name='password_reset_confirm'),
													path('password-reset/complete/',PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete'),
	]
