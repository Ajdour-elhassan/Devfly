from django.db import models

# Create your models here.

class Category(models.Model) :
    name = models.CharField(max_length=250 , unique=True)
    slug = models.SlugField(max_length=250 , unique=True)
    description = models.TextField(max_length=500 , blank=True)
    image = models.ImageField(upload_to='category' , blank=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self) :
        return self.name

class Post(models.Model) :
    title = models.CharField(max_length=250 , unique=250)
    slug = models.SlugField(max_length=250 , unique=True)
    details = models.TextField(max_length=250 , unique=True)
    image = models.ImageField(upload_to='Post' , blank=True)
    Category = models.ForeignKey(Category , on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta :
        ordering = ('title',)
        verbose_name = 'post'
        verbose_name_plural = 'posts'


    def __str__(self) :
        return self.title



