from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import DealsSerializer


class HomeViewSet(GenericViewSet):
    serializer_class = DealsSerializer
    queryset = User.objects.all()
