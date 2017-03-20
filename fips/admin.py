from django.contrib import admin
from .models import Category, Post, Comment, User, UploadFile, ImageComment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'title', 'author', 'created_date')

class CommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'post', 'author', 'created_date', 'approved_comment')

class ImageCommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'post', 'author', 'image', 'created_date', 'approved_comment')
      
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UploadFile)
admin.site.register(ImageComment, ImageCommentAdmin)
