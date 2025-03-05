from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField





class User(AbstractUser):
    email = models.EmailField(null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    country = models.CharField(max_length=256,null=True,blank=True)
    ph_no = models.IntegerField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    utimestamp =models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10)
    image = models.FileField(upload_to='user_images/',null=True,blank=True)
    

    def __str__(self):
        return self.email
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name')

    def __str__(self): 
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')


    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    thumbnail = models.ImageField(upload_to='thumbnail/',null=True,blank=True)
    post_image = models.FileField(upload_to='post_images/',null=True,blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = AutoSlugField(populate_from='title')


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): 
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True,blank=True)
    parent = models.ForeignKey('self',related_name="replies", on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True,blank=True)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    utimestamp =models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.text