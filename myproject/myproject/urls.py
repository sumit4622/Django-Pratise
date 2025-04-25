from pathlib import Path
import os

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from members.views import home

BASE_DIR = Path(__file__).resolve().parent.parent

urlpatterns = [
    path('members/', include('members.urls')),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
