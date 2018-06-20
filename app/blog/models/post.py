from django.contrib import admin
from django.db import models

from blog.models.commoninfo import CommonInfo

__all__ = (
    'Post',
    'PostLike',
    'PostAdmin',
    'PostLikeAdmin',
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


# 상속 받은 필드의 경우 Admin 페이지에서 볼 수 없어서
# 해당 필들르 보기 위해 아래와 같이 설정
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


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


class PostLikeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
