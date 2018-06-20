from django.contrib import admin

# Register your models here.
from .models.comment import CommentLikeAdmin, CommentAdmin
from .models.post import PostAdmin, PostLikeAdmin
from .models import Post, PostLike, Comment, CommentLike

admin.site.register(Post, PostAdmin)
admin.site.register(PostLike, PostLikeAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentLike, CommentLikeAdmin)
