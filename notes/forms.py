from django import forms
from django import forms
from django.forms import ModelForm

from .models import Note, Tag


class NotesCreationForm(ModelForm):
	
	class Meta:
		model = Note
		fields = ['title', 'body', 'tag']


# class TagCreationForm(ModelForm):

# 	class Meta:
# 		model = Tag
# 		fields = ['name']
