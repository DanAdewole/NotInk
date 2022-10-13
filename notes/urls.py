from django.urls import path

# from .views import NotesListView, NotesDetailView, notes_list_view
from .views import (
	NotesDeleteView, 
	notes_detail_view, 
	notes_list_view, 
	NotesUpdateView, 
	notesCreateView,
	tag_list_view,
	TagUpdateView,
	TagDeleteView,
	TagCreateView,
)

urlpatterns = [
	path('', notes_list_view, name='notes_list'),
	path('<int:pk>/', notes_detail_view, name='notes_detail'),
	path('<int:pk>/edit/', NotesUpdateView.as_view(), name='notes_update'),
	path('<int:pk>/delete/', NotesDeleteView.as_view(), name='notes_delete'),
	path('new/', notesCreateView, name='notes_new'),

	#labels
	path('labels/', tag_list_view, name="label_list"),
	path('labels/<int:pk>/edit/', TagUpdateView.as_view(), name="label_update"),
	path('labels/<int:pk>/delete/', TagDeleteView.as_view(), name='label_delete'),
	path('labels/new/', TagCreateView.as_view(), name='label_new'),
]

