from django.db import models
from django.conf import settings


class Note(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notes")
  slug = models.SlugField(unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.owner}'s {self.title}"