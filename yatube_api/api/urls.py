from django.urls import path, include

from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api.views import PostViewSet, GroupViewSet, FollowViewSet, CommentViewSet

app_name = 'api'

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments')

jwt_patterns = [
    path('jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(jwt_patterns)),
    # path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('v1/', include('djoser.urls.jwt')), 
]
