from django.contrib import admin
from .models import Project, Skill, Message


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "is_featured", "order", "created_at")
    list_editable = ("is_featured", "order")
    search_fields = ("title", "stack_tags")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "order")
    list_editable = ("order",)
    list_filter = ("category",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "read")
    list_filter = ("read",)
    readonly_fields = ("name", "email", "subject", "body", "created_at")
