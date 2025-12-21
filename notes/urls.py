from django.urls import path
from .views import (
    NoteListViewHome,
    NoteListView,
    NoteDetailView,
    NoteCreateView,
    NoteUpdateView,
    NoteDeleteView,
)


urlpatterns = [
    path("", NoteListViewHome.as_view(), name="note-list-home"),
    path("notes/", NoteListView.as_view(), name="note-list"),
    path("notes/create/", NoteCreateView.as_view(), name="note-create"),
    path("notes/<slug>/edit/", NoteUpdateView.as_view(), name="note-update"),
    path("notes/<slug>/delete/", NoteDeleteView.as_view(), name="note-delete"),
    path("notes/<slug>/", NoteDetailView.as_view(), name="note-detail"),
]
