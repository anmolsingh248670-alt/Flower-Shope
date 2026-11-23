
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse


urlpatterns = [
    path("admin/", admin.site.urls),

    # Google and Facebook login
    path("accounts/", include("allauth.urls")),

    # Your existing app URLs
    path("", include("app.urls")),
]


# Serve uploaded media files
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
