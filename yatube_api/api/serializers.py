from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, Follow, Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'pub_date', 'text', 'author', 'group', 'image')


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')


class GroupSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Follow
        fields = ('user', 'following')

    # возможно потребуется UniqueTogetherValidator, если недостаточно ограничений на уровне модели

    def validate(self, data):
        if data.get('user') == data.get('following'):
            raise serializers.ValidationError("Can't subscribe to yourself")
        return data
