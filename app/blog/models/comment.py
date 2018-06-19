from django.db import models

from members.models import BlogUser
from blog.models import Post

__all__ = (
    'Comment',
    'CommentLike',
)


class Comment(models.Model):
    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='my_comments',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        blank=True,
        null=True
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def like_users(self):
        return f'{self.comment_likes.all()}'

    def __str__(self):
        return f'{self.user}: {self.content}'


class CommentLike(models.Model):
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='comment_likes',
    )

    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='my_comment_likes',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}님이 ({self.comment})를 좋아합니다.'

