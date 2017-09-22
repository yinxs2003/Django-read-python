from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    release_date = models.DateField()
    num_starts = models.IntegerField()


class Comment(models.Model):
    post = models.ForeignKey(Post)
    name = models.CharField(max_length=100)
    comment = models.TextField()


class About(models.Model):
    about_me = models.CharField(max_length=999)
    about_my_blog = models.CharField(max_length=999)
    qq = models.CharField(max_length=999)
    git = models.CharField(max_length=999, default='')
    email = models.CharField(max_length=999)
