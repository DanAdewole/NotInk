from django.urls import path

from .views import NotesListView, NotesDetailView


urlpatterns = [
	path('', NotesListView.as_view(), name='notes_list'),
	path('detail/', NotesDetailView.as_view(), name='notes_detail'),
]

