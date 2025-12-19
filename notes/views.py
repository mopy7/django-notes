from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Note


class NoteListViewHome(ListView):
  model = Note
  template_name = "notes/home.html"
  context_object_name = "notes"

  def get_queryset(self):
    return Note.objects.order_by("-created_at")[:8]


class NoteListView(ListView):
  model = Note
  template_name = "notes/note_list.html"
  context_object_name = "notes"
  ordering = "-created_at"


class NoteDetailView(DetailView):
  model = Note
  template_name = "notes/note_detail.html"
  slug_field = "slug"
  slug_url_kwarg = "slug"

