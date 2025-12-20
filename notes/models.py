from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Note(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notes")
  slug = models.SlugField(unique=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.owner}'s {self.title}"
  
  def save(self, *args, **kwargs):
    if not self.slug:
      base_slug = slugify(self.title)
      slug = base_slug
      counter = 1

      while Note.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1
      
      self.slug = slug

    super().save(*args, **kwargs)
