from rest_framework.viewsets import GenericViewSet

from .models import Deal
from .serializers import DealsSerializer


class DealViewSet(GenericViewSet):
    serializer_class = DealsSerializer
    queryset = Deal.objects.all()

# class DealPostViewSet(GenericViewSet):
