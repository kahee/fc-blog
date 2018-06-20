from django.contrib import admin
from django.db import models

__all__ = (
    'CommonInfo',
    'CommonAdmin',
)


class CommonInfo(models.Model):
    user = models.ForeignKey(
        'members.BlogUser',
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CommonAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at')

    class Meta:
        abstract = True
