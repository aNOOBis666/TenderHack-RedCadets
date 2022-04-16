from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DealViewSet

router = DefaultRouter()
router.register('dealsList', DealViewSet)

urlpatterns = [
    path('deals/', include(router.urls)),
]