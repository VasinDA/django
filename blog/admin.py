from django.contrib import admin
from .models import Post, CommentPost

class CommentInline(admin.TabularInline):
    model = Post
    extra = 3 # how much empty lines to show

 
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
 
admin.site.register(Post, PostAdmin)
admin.site.register(CommentPost)