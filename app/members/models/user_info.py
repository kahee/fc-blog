from django.db import models

from . import BlogUser

__all__ = (
    'UserInfo',
)


class UserInfo(models.Model):
    user = models.OneToOneField(
        BlogUser,
        on_delete=models.CASCADE,
    )
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
