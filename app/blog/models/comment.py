from django.contrib import admin
from django.db import models

from .commoninfo import CommonInfo, CommonAdmin

__all__ = (
    'Comment',
    'CommentLike',
    'CommentAdmin',
    'CommentLikeAdmin',
)


class Comment(CommonInfo):
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
        """
        이 댓글에 좋아요를 누른 유저 리스트 리턴
        :return:
        """
        comments = self.comment_likes.all()
        return [comment.user for comment in comments]

    def __str__(self):
        return f'{self.user}: {self.content}'


class CommentAdmin(CommonAdmin):
    pass


class CommentLike(CommonInfo):
    comment = models.ForeignKey(
        'Comment',
        on_delete=models.CASCADE,
        related_name='comment_likes',
    )

    def __str__(self):
        return f'{self.user}님이 ({self.comment})를 좋아합니다.'


class CommentLikeAdmin(CommonAdmin):
    pass
