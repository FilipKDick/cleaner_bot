from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import (
    Chore,
    ChoreGroup,
    ChorePage,
)
from .serializers import (
    ChoreGroupSerializer,
    ChorePageSerializer,
    ChoreSerializer,
)


class ChorePageViewSet(
    RetrieveModelMixin,
    GenericViewSet,
):
    serializer_class = ChorePageSerializer
    queryset = ChorePage.objects.all()
    # TODO: limit pages to the ones user can access


class CreateChoreView(CreateAPIView):
    queryset = Chore.objects.all()
    serializer_class = ChoreSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChoreGroupListView(ListAPIView):
    queryset = ChoreGroup.objects.all()
    serializer_class = ChoreGroupSerializer
