from django.contrib import admin
from .models import Project, Skill, Message


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("short_code", "title", "category", "status", "is_featured", "order")
    list_editable = ("is_featured", "order", "status")
    list_filter = ("category", "status")
    search_fields = ("title", "stack_tags")
    prepopulated_fields = {"slug": ("title",)}


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
    actions = ["mark_read"]

    def mark_read(self, request, queryset):
        queryset.update(read=True)
    mark_read.short_description = "Marcar como lida"
