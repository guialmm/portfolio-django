from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    excerpt = models.TextField(max_length=300)
    body = models.TextField()
    cover = models.ImageField(upload_to="blog/", blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags")
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_tag_list(self):
        return [t.strip() for t in self.tags.split(",") if t.strip()]
