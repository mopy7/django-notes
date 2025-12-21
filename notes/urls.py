from django.urls import path
from .views import NoteListViewHome, NoteListView, NoteDetailView, NoteCreateView


urlpatterns = [
  path("", NoteListViewHome.as_view(), name="note-list-home"),
  path("notes/", NoteListView.as_view(), name="note-list"),
  path("notes/create/", NoteCreateView.as_view(), name="note-create"),
  path("notes/<slug>/", NoteDetailView.as_view(), name="note-detail"),
]