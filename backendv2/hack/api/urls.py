from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('all', CityViewSet)
router.register('preferences', CityPreferenceViewSet, basename='CityPreference')

urlpatterns = [
    path('', include(router.urls))
]