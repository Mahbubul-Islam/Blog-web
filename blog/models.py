from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(_("Blog Title"),max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # One category can have many post
    content = RichTextUploadingField()
    author = models.ForeignKey(User,on_delete=models.CASCADE) # One Author can have many Posts
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.PositiveBigIntegerField(default=0)
    liked_user = models.ManyToManyField(User, related_name='liked_post') # One Post can be liked by many Users, One User can like many Posts
    
    def __str__(self):
        return self.name
    
    
class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # One author can do many comment
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # One post can have multiple comment
    
    def __str__(self):
        return f"{self.author} commented on {self.post.title}"
    