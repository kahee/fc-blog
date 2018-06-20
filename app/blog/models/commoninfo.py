from django.db import models

__all__ = (
    'CommonInfo',
)


class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
