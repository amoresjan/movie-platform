from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from movies.views import MovieViewSet
from rest_framework.routers import DefaultRouter

ROUTER = DefaultRouter()

ROUTER.register("movies", MovieViewSet)

urlpatterns = path("", include(ROUTER.urls))
