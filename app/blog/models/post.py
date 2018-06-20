from django.contrib import admin
from django.db import models

from blog.models.commoninfo import CommonInfo, CommonAdmin

__all__ = (
    'Post',
    'PostLike',
    'PostAdmin',
    'PostLikeAdmin',
)


class Post(CommonInfo):
    title = models.CharField(max_length=100)
    content = models.TextField()

    @property
    def like_users(self):
        """
        이 글에 좋아요를 누른 유저 리스트 리턴
        :return:
        """
        posts = self.post_likes.all()
        return [post.user for post in posts]

    def __str__(self):
        return self.title


# 상속 받은 필드의 경우 Admin 페이지에서 볼 수 없어서
# 해당 필들르 보기 위해 아래와 같이 설정
class PostAdmin(CommonAdmin):
    pass


class PostLike(CommonInfo):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='post_likes',
    )

    def __str__(self):
        return f'{self.user}님이 ({self.post})를 좋아합니다.'


class PostLikeAdmin(CommonAdmin):
    pass
