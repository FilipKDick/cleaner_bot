from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import ChorePage
from .serializers import ChorePageSerializer


class ChorePageViewSet(
    RetrieveModelMixin,
    GenericViewSet,
):
    serializer_class = ChorePageSerializer
    queryset = ChorePage.objects.all()
    # TODO: limit pages to the ones user can access
