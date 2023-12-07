"""
URL configuration for yolo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import yolo.settings as settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi


urlpatterns = [
    path('admin/', admin.site.urls),

]

api_url_patterns = [
    path("api/", include("api.urls")),
]


api_docs_schema_view = get_schema_view(
    openapi.Info(
        title="Yolo module API",
        default_version="v1",
    ),
    patterns=api_url_patterns,
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)

api_docs_urlpatterns = [
    path(
        "api/swagger/",
        api_docs_schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    )
]

urlpatterns += (
    api_url_patterns
    + api_docs_urlpatterns
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
