from rest_framework import routers

from .views import ChorePageViewSet

app_name = 'chores'

router = routers.DefaultRouter()
router.register('', ChorePageViewSet, basename='chore_page')
urlpatterns = router.urls
