from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
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
  

class NoteCreateView(LoginRequiredMixin, CreateView):
  model = Note
  fields = ["title", "content"]
  template_name = "notes/note_form.html"
  
  def form_valid(self, form):
    form.instance.owner = self.request.user
    return super().form_valid(form)
  
  def get_success_url(self):
    return reverse("note-detail", kwargs={"slug": self.object.slug})
  

  