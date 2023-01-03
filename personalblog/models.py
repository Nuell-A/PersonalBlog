from django.db import models
# User being the author of the post.
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200, default='Blaggers')
    # When an author is deleted, then so will all the posts from them.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        # A query will result in the post title and author
        return self.title + ' | ' + str(self.author)