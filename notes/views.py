from django.shortcuts import render
from django.views.generic import TemplateView



class NotesListView(TemplateView):
	template_name = 'notes_list.html'


class NotesDetailView(TemplateView):
	template_name: str = 'notes_detail.html'
