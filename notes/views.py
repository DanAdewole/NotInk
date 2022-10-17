from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

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


def notes_detail_view(request, pk):
	note = Note.objects.get(id=pk)
	tag_name = Tag.objects.get(id=note.tag_id)
	note.tag_id = tag_name
	context = {'note': note}
	return render(request, 'notes_detail.html', context)


class NotesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Note
	template_name: str = 'notes_update.html'
	fields = ('title', 'body')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user


class NotesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Note
	template_name: str = 'notes_delete.html'
	success_url = reverse_lazy('notes_list')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user


# class NotesCreateView(CreateView):
# 	model = Note
# 	template_name: str = 'notes_new.html'
# 	fields = ('title', 'body', 'author', 'tag')


def notesCreateView(request):
	form = NotesCreationForm()
	current_user = request.user
	form.fields["tag"].queryset = Tag.objects.filter(user_id=current_user.id)

	if request.method == "POST":
		form = NotesCreationForm(request.POST)
		current_user = request.user
		form.fields["tag"].queryset = Tag.objects.filter(user_id=current_user.id)

		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('notes_detail', instance.id)

	context = {'form': form}
	return render(request, 'notes_new.html', context)


# Views catering for Labels
def tag_list_view(request):
	user_id = request.user.id
	tags = Tag.objects.filter(user_id=user_id)
	context = {'tags': tags}
	return render(request, 'labels.html', context)


class TagUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Tag
	template_name: str = 'labels_update.html'
	fields = ('name',)
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.user == self.request.user


class TagDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Tag
	template_name: str = 'labels_delete.html'
	success_url = reverse_lazy('label_list')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.user == self.request.user


class TagCreateView(LoginRequiredMixin, CreateView):
	model = Tag
	template_name: str = 'labels_new.html'
	fields = ('name',)
	login_url = 'login'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

