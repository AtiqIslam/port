from django.contrib import admin

from .models import Project, Resume


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "tech_stack", "created_at")
    search_fields = ("title", "description", "tech_stack")
    list_filter = ("created_at",)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "uploaded_at")
    list_editable = ("is_active",)
    list_filter = ("is_active", "uploaded_at")
