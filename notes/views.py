from this import d
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView

from .models import Note, Tag
from .forms import NotesCreationForm


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


# class NotesDetailView(DetailView):
# 	model = Note
# 	template_name: str = 'notes_detail.html'
# 	context_object_name: str = 'note'

# 	def get_context_data(self, *args, **kwargs):
# 		context = super(NotesDetailView, self).get_context_data(*args, **kwargs)
# 		note_id = self.request.notes.id
# 		print(note_id)
# 		# note = Note.objects.filter(author_id=user_id)
# 		# for note in notes:
# 		# 	tag_name = Tag.objects.get(id=note.tag_id)
# 		# 	note.tag_id = tag_name

# 		return context

def notes_detail_view(request, pk):
	note = Note.objects.get(id=pk)
	tag_name = Tag.objects.get(id=note.tag_id)
	note.tag_id = tag_name
	context = {'note': note}
	return render(request, 'notes_detail.html', context)


class NotesUpdateView(UpdateView):
	model = Note
	template_name: str = 'notes_update.html'
	fields = ('title', 'body')


class NotesDeleteView(DeleteView):
	model = Note
	template_name: str = 'notes_delete.html'
	success_url = reverse_lazy('notes_list')


# class NotesCreateView(CreateView):
# 	model = Note
# 	template_name: str = 'notes_new.html'
# 	fields = ('title', 'body', 'author', 'tag')


def notesCreateView(request):
	form = NotesCreationForm()

	if request.method == "POST":
		form = NotesCreationForm(request.POST)

		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('notes_detail', instance.id)

	context = {'form': form}
	return render(request, 'notes_new.html', context)


# Views catering for Labels
def tag_list_view(request):
	tags = Tag.objects.all()
	context = {'tags': tags}
	return render(request, 'labels.html', context)


class TagUpdateView(UpdateView):
	model = Tag
	template_name: str = 'labels_update.html'
	fields = ('name',)


class TagDeleteView(DeleteView):
	model = Tag
	template_name: str = 'labels_delete.html'
	
