from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model) :
    name = models.CharField(max_length=250 , unique=True)
    slug = models.SlugField(max_length=250 , unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    # get Post_by_category
    def get_url(self) :
        return reverse('post_by_category' , args=[self.slug])

    def __str__(self) :
        return self.name

class Post(models.Model) :
    title = models.CharField(max_length=250 , unique=250)
    slug = models.SlugField(max_length=250 , unique=True)
    details = models.TextField()
    image = models.ImageField(upload_to='Post' , blank=True)
    Category = models.ForeignKey(Category , on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('post_details' , args=[self.Category.slug , self.slug])
    class Meta :
        ordering = ('title',)
        verbose_name = 'post'
        verbose_name_plural = 'posts'


    def __str__(self) :
        return self.title

class Feedback(models.Model) :
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    def __str__(self) :
        return self.content 


class Contact(models.Model) :
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=400)
    message = models.TextField()
    
    def __str__(self) :
        return self.name




