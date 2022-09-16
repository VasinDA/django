from django.contrib import admin
from .models import Article, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 2 # how much empty lines to show

 
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)

