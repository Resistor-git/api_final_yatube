from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Group
from api.serializers import (
    PostSerializer, CommentSerializer, FollowSerializer, GroupSerializer
)
from api.permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet to create, retrieve, update and delete posts.
    Author is provided automatically from request.
    Posts can be modified or deleted only by their authors.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet to retrieve groups.
    Groups can not be created or changed using API.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet to create, retrieve, update and delete comments.
    Comment can be created only for existing Post.
    Author is provided automatically from request.
    Comments can be modified or deleted only by their authors.
    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

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
    """
    ViewSet to create, retrieve, update and delete subscriptions (follows).
    Follows are available only for authenticated users.
    """
    serializer_class = FollowSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username']

    def get_queryset(self):
        user = self.request.user
        return user.subscriptions.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
