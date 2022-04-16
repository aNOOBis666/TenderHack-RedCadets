from rest_framework.viewsets import GenericViewSet

from .models import Deal, User
from .serializers import DealsSerializer, UserSerializer


class DealViewSet(GenericViewSet):
    serializer_class = DealsSerializer
    queryset = Deal.objects.all()

# class DealPostViewSet(GenericViewSet):

class UserViewSet(GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()