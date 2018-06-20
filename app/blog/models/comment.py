from django.contrib import admin
from django.db import models

from .commoninfo import CommonInfo

__all__ = (
    'Comment',
    'CommentLike',
    'CommentAdmin',
    'CommentLikeAdmin',
)


class Comment(CommonInfo):
    user = models.ForeignKey(
        'members.BlogUser',
        on_delete=models.CASCADE,
        related_name='my_comments',
    )
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comments',
        blank=True,
        null=True
    )
    content = models.TextField()

    @property
    def like_users(self):
        return f'{self.comment_likes.all()}'

    def __str__(self):
        return f'{self.user}: {self.content}'


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


class CommentLike(CommonInfo):
    comment = models.ForeignKey(
        'Comment',
        on_delete=models.CASCADE,
        related_name='comment_likes',
    )

    user = models.ForeignKey(
        'members.BlogUser',
        on_delete=models.CASCADE,
        related_name='my_comment_likes',
    )

    def __str__(self):
        return f'{self.user}님이 ({self.comment})를 좋아합니다.'


class CommentLikeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
