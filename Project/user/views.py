from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from .forms import RegisterForm,CredentialForm,ProfileForm,PostForm
from django.contrib.auth.decorators import login_required
from . models import Post,Friend

# def change_friend(request,operation,pk):
# 	new_friend = get_object_or_404(Friend,pk=pk)
# 	if operation=='add':
# 		Friend.make_friend(current_user,new_friend)
# 	elif operation =='remove':
# 		Friend.lose_friend(current_user,new_friend)
# 	return redirect('user:home')





def home_view(request):
	''' View handling the home page of the social networking sites '''
	posts = Post.objects.all().order_by('-date')
	users = User.objects.exclude(id=request.user.id)#gets everthing except for the user logged in
	#Friend is searching for the current user logged in 
	# friend = Friend.objects.get(current_user=request.user)
	# #This is showing all the users
	# friends = friend.users.all()


	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect('user:home')
	else:
		form = PostForm()
	template_name = 'user/home.html'
	args = {'form' : form,'posts':posts,'users':users}
	return render(request,template_name,args)



@login_required
def profile(request,pk=None):
	'''checking whether the user has pressed the other user or not !

		if the primary key(pk) is not there meaning if the user do not click any other users
		name link then get me the current user(i.e current_user ) 

		else get me the information of the user by pk of that user and assign it to other user

	'''
	posts = Post.objects.all().order_by('-date')
	if not(pk):
		current_user = request.user
		if request.method == 'POST':
			p_form = ProfileForm(request.POST or None ,request.FILES,instance=request.user.profile)
			user_form = CredentialForm(request.POST,instance=request.user)
			if p_form.is_valid() and user_form.is_valid():
				p_form.save()
				user_form.save()
				return redirect('user:profile')
		else:
			p_form = ProfileForm(instance=request.user.profile)
			user_form = CredentialForm(instance=request.user)
			args = {'p_form':p_form,'user_form':user_form,'current_user':current_user}
			

	else:
		other_user = User.objects.get(pk=pk)
		if request.method == 'POST':
			p_form = ProfileForm(request.POST or None ,request.FILES,instance=other_user.profile)
			user_form = CredentialForm(request.POST,instance=other_user)
			if p_form.is_valid() and user_form.is_valid():
				p_form.save()
				user_form.save()
				return redirect('user:profile')
		else:
			p_form = ProfileForm(instance=other_user.profile)
			user_form = CredentialForm(instance=other_user)
			args = {'p_form':p_form,'user_form':user_form,'other_user':other_user}
		
	
	template_name = 'user/profile.html'
	return render(request,template_name,args)

	
	


def register_view(request):
	''' View handling the registration of the user'''
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data.get('username')
			user.save()
			return redirect('user:login')
	else:
		form = RegisterForm()

	template_name = 'user/register.html'
	args = {'form' : form}
	return render(request,template_name,args)


def login_view(request):
	'''  view handling the authentication of the user '''
	if request.method == 'POST':
		form = AuthenticationForm(request,request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				messages.info(request,f'Successfully logged in!')
				return redirect('user:home')
			
	else:
		form = AuthenticationForm()

	template_name = 'user/login.html'
	args = {'form' : form}
	return render(request,template_name,args)


@login_required
def logout_view(request):
	''' View handling the Logging out of the page'''
	logout(request)
	return redirect('user:login')



@login_required
def password_change_view(request):
	''' View handling the changing password of the person '''
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST,user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			return redirect('user:profile')
	else:
		form = PasswordChangeForm(user=request.user)
	template_name = 'user/password_change.html'
	args = {'form' : form}
	return render(request,template_name,args)










