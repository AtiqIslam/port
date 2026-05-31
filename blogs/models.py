from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=180)
    content = models.TextField()
    image = models.ImageField(upload_to="blogs/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
