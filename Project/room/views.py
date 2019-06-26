from django.shortcuts import render,redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from . forms import Rentform
from . models import Room
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(request):
	rooms = Room.objects.all()
	context = {'rooms':rooms}
	return render(request, 'room/rooms_info.html' ,context)

def profile(request):
	return render(request,'room/profile.html' ,{})

def about(request):
	return render(request , 'room/about.html',{})


def post_rent(request):
	if request.method=='POST':
		form = Rentform(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('room:home')
		else:
			messages.error(request,f'invalid')

	form = Rentform()
	context = {"form":form}
	return render(request,'room/rent_post.html',context)

