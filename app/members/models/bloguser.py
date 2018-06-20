from django.db import models

__all__ = (
    'BlogUser',
)


class BlogUser(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField(
        'self',
        related_name='my_friends',
        symmetrical=False,
        # blank=True,
    )
    block_users = models.ManyToManyField(
        'self',
        related_name='block_friends',
        symmetrical=False,
        # blank=True,
    )

    @property
    def comments(self):
        """
        자신이 작성한 모든 댓글 QuerySet리턴
        :return:
        """
        # return f'내가 작성한 댓글 목록 : {Comment.objects.filter(user=self)}'
        return f'내가 작성한 댓글 목록: {self.my_comments.all()}'

    @property
    def posts(self):
        """
        자신이 작성한 모든 글 QuerySet리턴
        :return:
        """
        return f'내가 작성한 글 목록: {self.my_posts.all()}'

    def __str__(self):
        return self.name
