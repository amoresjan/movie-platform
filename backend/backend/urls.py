from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from movies.urls import urlpatterns as MOVIE_URLS

urlpatterns = [path("admin/", admin.site.urls), path("api/", include([MOVIE_URLS]))]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
