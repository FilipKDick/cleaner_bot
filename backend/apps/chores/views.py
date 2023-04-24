from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    get_object_or_404,
)
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
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


class ChoreMarkCompletedView(APIView):
    serializer = ChoreSerializer

    def post(self, request, *args, **kwargs):
        chore_id = request.data.get('chore_id', None)
        chore = get_object_or_404(Chore, id=chore_id)
        chore.mark_done()
        serializer = self.serializer(instance=chore)
        return Response(serializer.data)
