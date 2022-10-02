from django.urls import path
from rest_framework import routers

from .views import (
    ChorePageViewSet,
    CreateChoreView,
)

app_name = 'chores'

router = routers.DefaultRouter()
router.register('pages', ChorePageViewSet, basename='chore_page')

urlpatterns = [
    path('create/', CreateChoreView.as_view()),
    *router.urls,
]
