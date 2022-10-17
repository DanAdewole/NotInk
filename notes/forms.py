from django import forms
from django.forms import ModelForm

from .models import Note


class NotesCreationForm(ModelForm):
	
	class Meta:
		model = Note
		fields = ['title', 'body', 'tag']
		error_messages = {
			'tag': {
				'required': ("Select a tag, if none, create a label."),
			}
		}
