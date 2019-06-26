from django import forms 
from django.contrib.auth.models import User
from . models import Room



class Rentform(forms.ModelForm):
	class Meta:
		model = Room
		fields = ('rooms_name','location','owner_name','owner_number',
			'rooms_summary','number_of_room','rooms_pic',)
		widgets = {
			'rooms_name' : forms.TextInput(attrs={'class':'form-control'}),
			'location' : forms.TextInput(attrs={'class':'form-control'}),
			'owner_name': forms.TextInput(attrs={'class':'form-control'}),
			'owner_number' : forms.TextInput(attrs={'class':'form-control'}),
			'rooms_summary' : forms.TextInput(attrs={'class':'form-control'}),
			'number_of_room' : forms.TextInput(attrs={'class':'form-control'}),
			
		}

