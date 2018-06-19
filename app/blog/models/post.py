from django.db import models

from members.models import BlogUser

__all__ = (
    'Post',
    'PostLike',
)


class Post(models.Model):
    user = models.ForeignKey(
        'members.BlogUser',
        on_delete=models.CASCADE,
        related_name='my_posts',
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def like_users(self):
        return f'{self.post_likes.all()}'

    def __str__(self):
        return self.title


class PostLike(models.Model):
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
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}님이 ({self.post})를 좋아합니다.'
