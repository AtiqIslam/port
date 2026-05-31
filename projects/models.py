from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    tech_stack = models.CharField(max_length=255, help_text="Comma-separated technologies")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Resume(models.Model):
    title = models.CharField(max_length=120, default="Atiqul Islam Rahad Resume")
    file = models.FileField(upload_to="resumes/")
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return self.title
