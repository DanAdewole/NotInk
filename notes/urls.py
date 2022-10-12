from django.urls import path

# from .views import NotesListView, NotesDetailView, notes_list_view
from .views import (
	NotesDeleteView, 
	notes_detail_view, 
	notes_list_view, 
	NotesUpdateView, 
	notesCreateView,
	
)

urlpatterns = [
	path('', notes_list_view, name='notes_list'),
	path('<int:pk>/', notes_detail_view, name='notes_detail'),
	path('<int:pk>/edit/', NotesUpdateView.as_view(), name='notes_update'),
	path('<int:pk>/delete/', NotesDeleteView.as_view(), name='notes_delete'),
	path('new/', notesCreateView, name='notes_new'),
]

