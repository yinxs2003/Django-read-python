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
