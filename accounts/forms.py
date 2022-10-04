from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('username', 'email', 'password1', 'password2',)

	def __init__(self, *args, **kwargs):
		super(CustomUserCreationForm, self).__init__(*args, **kwargs)
		
		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None


class CustomUserChangeForm(UserChangeForm):

	class Meta(UserChangeForm):
		model = CustomUser
		fields = ('username', 'email')

