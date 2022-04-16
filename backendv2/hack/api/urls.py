from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import HomeViewSet

router = DefaultRouter()
router.register('dealsList', HomeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]