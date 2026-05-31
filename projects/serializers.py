from rest_framework import serializers

from .models import Project, Resume


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "description",
            "image",
            "github_link",
            "live_link",
            "tech_stack",
            "created_at",
        )
        read_only_fields = ("created_at",)


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ("id", "title", "file", "is_active", "uploaded_at")
        read_only_fields = ("uploaded_at",)
