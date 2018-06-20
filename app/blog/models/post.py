from django.contrib import admin
from django.db import models

from blog.models.commoninfo import CommonInfo

__all__ = (
    'Post',
    'PostLike',
)


class Post(CommonInfo):
    user = models.ForeignKey(
        'members.BlogUser',
        on_delete=models.CASCADE,
        related_name='my_posts',
    )
    title = models.CharField(max_length=100)
    content = models.TextField()

    @property
    def like_users(self):
        return f'{self.post_likes.all()}'

    def __str__(self):
        return self.title


class PostLike(CommonInfo):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='post_likes',
    )
    user = models.ForeignKey(
        'members.BlogUser',
        on_delete=models.CASCADE,
        related_name='my_post_likes',
    )

    def __str__(self):
        return f'{self.user}님이 ({self.post})를 좋아합니다.'
