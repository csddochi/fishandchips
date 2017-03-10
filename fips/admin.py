from django.contrib import admin
from .models import Category, Post, Comment, User

# Register your models here.
class PostAdmin(admin.ModelAdmin):
      list_display = ('id', 'subject', 'title', 'author', 'created_date')
      
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
