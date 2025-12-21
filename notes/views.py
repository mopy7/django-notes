from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note


class NoteListViewHome(LoginRequiredMixin, ListView):
  model = Note
  template_name = "notes/home.html"
  context_object_name = "notes"

  def get_queryset(self):
    return Note.objects.filter(owner=self.request.user).order_by("-created_at")[:8]


class NoteListView(LoginRequiredMixin, ListView):
  model = Note
  template_name = "notes/note_list.html"
  context_object_name = "notes"
  
  def get_queryset(self):
    return Note.objects.filter(owner=self.request.user).order_by("-created_at")

class NoteDetailView(LoginRequiredMixin, DetailView):
  model = Note
  template_name = "notes/note_detail.html"
  slug_field = "slug"
  slug_url_kwarg = "slug"
  context_object_name = "note"

  def get_queryset(self):
    return Note.objects.filter(owner=self.request.user)
  
