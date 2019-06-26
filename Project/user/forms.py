from django import forms 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from . models import Profile,Post



class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('text',)
		widgets = {
				'text' : forms.TextInput(attrs={'class':'form-control','placeholder':'What is in your mind?'}),
		}

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('bio_data','city','website','image')

		widgets = {
				'bio_data' : forms.TextInput(attrs={'class':'form-control'}),
				'city' : forms.TextInput(attrs={'class':'form-control'}),
				'website' : forms.TextInput(attrs={'class':'form-control'}),
		}

class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)
	phone_number = forms.IntegerField()
	class Meta:
		model= User
		fields = ('username','first_name','last_name','email','password1','password2','phone_number')
		widgets = {
				'username' : forms.TextInput(attrs={'class':'form-control'}),
				'first_name' : forms.TextInput(attrs={'class':'form-control'}),
				'last_name' : forms.TextInput(attrs={'class':'form-control'}),
				'email' : forms.TextInput(attrs={'class':'form-control'}),
				'password1' : forms.PasswordInput(attrs={'class':'form-control'}),
				'password2' : forms.PasswordInput(attrs={'class':'form-control'}),


		}

	def clean_email(self):
		email = self.cleaned_data['email']
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise ValidationError('Already registered with that email')
		return email
	


class CredentialForm(UserChangeForm):
	class Meta:
		model= User
		fields = ('username','first_name','last_name','password')
		widgets = {
				'username' : forms.TextInput(attrs={'class':'form-control'}),
				'first_name' : forms.TextInput(attrs={'class':'form-control'}),
				'last_name' : forms.TextInput(attrs={'class':'form-control'}),
		}

	