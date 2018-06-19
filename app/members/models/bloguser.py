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
    )
    block_users = models.ManyToManyField(
        'self',
        related_name='block_friends',
        symmetrical=False,
    )
