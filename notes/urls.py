from django.urls import path
from .views import NoteListViewHome, NoteListView, NoteDetailView


urlpatterns = [
  path("", NoteListViewHome.as_view(), name="note-list-home"),
  path("notes/", NoteListView.as_view(), name="note-list"),
  path("notes/<slug>/", NoteDetailView.as_view(), name="note-detail"),
]