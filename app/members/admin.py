from django.contrib import admin

# Register your models here.
from .models import BlogUser, UserInfo

admin.site.register(BlogUser)
admin.site.register(UserInfo)
