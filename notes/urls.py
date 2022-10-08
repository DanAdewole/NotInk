from django.urls import path

# from .views import NotesListView, NotesDetailView, notes_list_view
from .views import NotesDetailView, notes_list_view

urlpatterns = [
	path('', notes_list_view, name='notes_list'),
	path('<int:pk>', NotesDetailView.as_view(), name='notes_detail'),
]

