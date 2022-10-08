from webbrowser import get
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView

from .models import Note, Tag


# class NotesListView(TemplateView):
# 	template_name = 'notes_list.html'


def notes_list_view(request):
	user_id = request.user.id
	notes = Note.objects.filter(author_id=user_id).order_by('-date_updated')
	for note in notes:
		if len(note.body) > 40:
			note.body = f"{note.body[:40]}..."
		tag_name = Tag.objects.get(id=note.tag_id)
		note.tag_id = tag_name
	
	context = {'notes': notes}
	return render(request, 'notes_list.html', context)


class NotesDetailView(DetailView):
	model = Note
	template_name: str = 'notes_detail.html'
	context_object_name: str = 'note'


class NotesUpdateView(UpdateView):
	model = Note
	template_name: str = 'notes_update.html'
	fields = ('title', 'body')


class NotesDeleteView(DeleteView):
	model = Note
	template_name: str = 'notes_delete.html'
	success_url = reverse_lazy('notes_list')
