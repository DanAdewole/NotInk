from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.db.models import Q

from .models import Note, Tag
from .forms import NotesCreationForm


@login_required
def notes_list_view(request):
	user_id = request.user.id
	notes = Note.objects.filter(author_id=user_id).order_by('-date_updated')
	for note in notes:
		if len(note.body) > 40:
			note.body = f"{note.body[:40]}..."
		if len(note.title) > 20:
			note.title = f"{note.title[:20]}..."
		tag_name = get_object_or_404(Tag, id=note.tag_id)
		# tag_name = Tag.objects.get(id=note.tag_id)
		note.tag_id = tag_name
	
	context = {'notes': notes}
	return render(request, 'notes_list.html', context)


@login_required
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


@login_required
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
@login_required
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

	# user passes test mixin parameter
	def test_func(self):
		obj = self.get_object()
		return obj.user == self.request.user


class TagDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Tag
	template_name: str = 'labels_delete.html'
	success_url = reverse_lazy('label_list')
	login_url = 'login'

	# user passes test mixin parameter
	def test_func(self):
		obj = self.get_object()
		return obj.user == self.request.user


class TagCreateView(LoginRequiredMixin, CreateView):
	model = Tag
	template_name: str = 'labels_new.html'
	fields = ('name',)
	login_url = 'login'

	# automatically save current user as author
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


# views for sidebar label list
@login_required
def tag_filter_list_view(request, tag):
	current_user = request.user
	tag_id = Tag.objects.get(name=tag, user_id=current_user.id)
	notes = Note.objects.filter(tag_id=tag_id).order_by('-date_updated')

	for note in notes:
		if len(note.body) > 40:
			note.body = f"{note.body[:40]}..."
		if len(note.title) > 20:
			note.title = f"{note.title[:20]}..."
		tag_name = Tag.objects.get(id=note.tag_id)
		note.tag_id = tag_name

	context = {
		'notes': notes,
		'tag': tag,
	}
	return render(request, 'labels_filter_list.html', context)


class SearchResultsView(LoginRequiredMixin, ListView):
	model = Note
	template_name: str = 'search_results.html'
	context_object_name = 'search_results'

	def get_queryset(self):
		query = self.request.GET.get("q", None)
		current_user = self.request.user
		context = Note.objects.filter(
			author_id=current_user.id
		).filter(
			Q(title__icontains=query) | Q(body__icontains=query)
		)

		for note in context:
			if len(note.body) > 40:
				note.body = f"{note.body[:40]}..."
			if len(note.title) > 20:
				note.title = f"{note.title[:20]}..."
			tag_name = Tag.objects.get(id=note.tag_id)
			note.tag_id = tag_name
			
		return context


def error_404_view(request, exception):
	return render(request, '404.html')

def error_500_view(request):
	return render(request, '500.html')
