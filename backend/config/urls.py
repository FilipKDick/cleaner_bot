from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (
    include,
    path,
)
from rest_framework.authtoken.views import obtain_auth_token

# API URLS
api_urlpatterns = [
    # DRF auth token
    path('auth-token/', obtain_auth_token),
    path('users/', include('apps.users.api.urls', namespace='users')),
    path('chores/', include('apps.chores.urls', namespace='chores')),
]

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/v1/', include(api_urlpatterns)),  # type: ignore
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
