from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import RegisterAPIView
from blogs.views import BlogViewSet, blog_list
from contacts.views import ContactAPIView, contact_page
from projects.views import ProjectViewSet, ResumeDownloadView, about, home, project_list

admin.site.site_header = "Atiqul Islam Rahad Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Dashboard"

schema_view = get_schema_view(
    openapi.Info(
        title="Atiqul Islam Rahad Portfolio API",
        default_version="v1",
        description="Projects, blogs, contact messages, authentication, and resume APIs.",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register("projects", ProjectViewSet, basename="project")
router.register("blogs", BlogViewSet, basename="blog")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("projects/", project_list, name="projects"),
    path("blog/", blog_list, name="blog"),
    path("contact/", contact_page, name="contact"),
    path("resume/download/", ResumeDownloadView.as_view(), name="resume-download"),
    path("api/", include(router.urls)),
    path("api/contact/", ContactAPIView.as_view(), name="api-contact"),
    path("api/auth/register/", RegisterAPIView.as_view(), name="api-register"),
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
