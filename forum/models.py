from django.db import models
from django.contrib.auth.models import User
from auth_app.models import * 
import datetime
from django.utils.timezone import now



class ForumModerator(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, verbose_name='Related User Model')

    def __str__(self):

        return self.user.email

class ForumPost(models.Model):
    user = models.ForeignKey(
        to=CustomUser, 
        on_delete=models.CASCADE, 
        verbose_name='Related User',
        related_name='forum_posts'
    )
    content = models.TextField(verbose_name='Post Content')
    
    upvote_users = models.ManyToManyField(
        to=CustomUser, 
        verbose_name="Users Who Upvoted", 
        related_name="upvoted_posts"
    )
    downvote_users = models.ManyToManyField(
        to=CustomUser, 
        verbose_name="Users Who Downvoted", 
        related_name="downvoted_posts"
    )
    approved = models.BooleanField(default=False, verbose_name="Approval Status")

    date_time = models.DateTimeField(default=now)


    def __str__(self):
        return self.user.email


class ForumPostReply(models.Model):

    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, verbose_name='Related User Model')
    content = models.TextField()

    post = models.ForeignKey(to=ForumPost, on_delete=models.CASCADE, verbose_name='Related Post')

    def __str__(self):

        return
