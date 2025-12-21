from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
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


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ["title", "content"]
    template_name = "notes/note_form.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse("note-detail", kwargs={"slug": self.object.slug})


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = "notes/note_confirm_delete.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("note-list")

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)


