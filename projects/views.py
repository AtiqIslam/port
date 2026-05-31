from django.http import FileResponse, Http404
from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.views import APIView

from blogs.models import Blog
from .models import Project, Resume
from .serializers import ProjectSerializer


def _home_context():
    return {
        "projects": Project.objects.all()[:6],
        "blogs": Blog.objects.all()[:3],
        "skills": [
            ("Python", 88),
            ("Django", 84),
            ("Django REST Framework", 82),
            ("PostgreSQL", 76),
            ("Git", 78),
            ("HTML", 72),
            ("CSS", 70),
            ("Bootstrap", 75),
        ],
    }


def home(request):
    return render(request, "home.html", _home_context())


def about(request):
    return render(request, "about.html")


def project_list(request):
    return render(request, "projects.html", {"projects": Project.objects.all()})


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class ResumeDownloadView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        resume = Resume.objects.filter(is_active=True).first()
        if not resume or not resume.file:
            raise Http404("No active resume has been uploaded yet.")
        return FileResponse(resume.file.open("rb"), as_attachment=True, filename=resume.file.name.split("/")[-1])
