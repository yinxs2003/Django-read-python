# coding=utf-8
# 后台
from django.contrib import admin

from blog.models import Post, Comment, About


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('about_me',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('about_me',)
