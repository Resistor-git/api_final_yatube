from django.contrib import admin

from .models import Post, Group, Comment, Follow


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-empty-'


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description')
    list_editable = ('title', 'description',)
    search_fields = ('title',)
    empty_value_display = '-empty-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'created', 'post', 'author',)
    list_editable = ('text',)
    search_fields = ('text',)
    list_filter = ('author',)
    empty_value_display = '-empty-'


class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'following')
    list_editable = ('following',)
    search_fields = ('following',)
    empty_value_display = '-empty-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
