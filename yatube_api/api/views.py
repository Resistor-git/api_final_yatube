# TODO:
# Post -list (get, post)
#   -- auth or readonly
#   -- limit, offcet
# Post -detail (get, post, patch, delete)
#   -- owner
# Comment -list (get, post)
# Comment -detail (get, post, patch, delete)
#  -- owner
# Follow -list (get)
#   -- auth(!)
# Follow -detail ((get, post, patch, delete)
#   -- auth, request.user = obj.user

from rest_framework import viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post
from api.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
