from django.urls import path, include

from rest_framework.routers import SimpleRouter

from api.views import PostViewSet

app_name = 'api'

router = SimpleRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
