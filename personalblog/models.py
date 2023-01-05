from django.db import models
# User being the author of the post.
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200)
    # When an author is deleted, then so will all the posts from them.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        # A query will result in the post title and author
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        '''
        This method is created so that the website knows where
        to go when it needs to be redirected (after the post button)
        '''
        # Below we use reverse() and give it the url to return to (name)
        #  and we also give it the id of the newly created post so that it knows 
        #   which  post to go to. 
        return reverse('post_details', args=(str(self.id)))

        # An example of redirecting to the home page (doesn't need any args due to no
        #  specific id in the url needed)
        #return reverse('home')