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

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Group
from api.serializers import (
    PostSerializer, CommentSerializer, FollowSerializer, GroupSerializer
)
from api.permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated & IsAuthorOrReadOnly)

    def get_post_id(self):
        return self.kwargs.get("post_id")

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.get_post_id())
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(
            post=get_object_or_404(Post, id=self.get_post_id()),
            author=self.request.user
        )


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer

    def get_queryset(self):
        user = self.request.user
        return user.subscriptions.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
