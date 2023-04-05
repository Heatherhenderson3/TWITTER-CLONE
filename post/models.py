from django.db import models
from cloudinary.models import CloudinaryField

class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', null = False, blank = False, max_length= 20, default= 'Jane Doe'
     )
    body = models.CharField(
        'body', null = True, blank= True, max_length= 500
    )
    created_at = models.DateTimeField(
        'Post Time', blank = True, auto_now_add=True
    )
    image = CloudinaryField(
        'image',blank=True,db_index=True
    )
    likecount = models.IntegerField(
        'like_count',default=0,null=True,blank=True
    )

    def __str__(self):
        return self.name
    