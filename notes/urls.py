from django.urls import path

from .views import NotesListView


urlpatterns = [
	path('', NotesListView.as_view(), name='notes_list'),
]


