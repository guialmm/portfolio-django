from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    stack_tags = models.CharField(max_length=300, help_text="Comma-separated: Python, Django, PostgreSQL")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title

    def get_stack_list(self):
        return [tag.strip() for tag in self.stack_tags.split(",") if tag.strip()]


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("lang", "Linguagens"),
        ("framework", "Frameworks"),
        ("ai", "IA / ML"),
        ("tool", "Ferramentas"),
        ("db", "Banco de Dados"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["category", "order"]

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Message(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.subject}"
