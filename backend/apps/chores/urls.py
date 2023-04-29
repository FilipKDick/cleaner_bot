from django.urls import path
from rest_framework import routers

from .views import (
    ChoreGroupViewSet,
    ChoreMarkCompletedView,
    ChorePageViewSet,
    CreateChoreView,
)

app_name = 'chores'

router = routers.DefaultRouter()
router.register('pages', ChorePageViewSet, basename='chore_page')
router.register('groups', ChoreGroupViewSet, basename='groups')

urlpatterns = [
    path('create/', CreateChoreView.as_view()),
    path('mark_done/', ChoreMarkCompletedView.as_view()),
    *router.urls,
]
