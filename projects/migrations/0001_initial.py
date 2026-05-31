from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=160)),
                ("description", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="projects/")),
                ("github_link", models.URLField(blank=True)),
                ("live_link", models.URLField(blank=True)),
                ("tech_stack", models.CharField(help_text="Comma-separated technologies", max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="Resume",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(default="Atiqul Islam Rahad Resume", max_length=120)),
                ("file", models.FileField(upload_to="resumes/")),
                ("is_active", models.BooleanField(default=True)),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-uploaded_at"]},
        ),
    ]
