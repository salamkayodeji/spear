from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from typing import Optional
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query import QuerySet
from slugify import slugify
from django.db.models.signals import pre_save
from django.utils.text import slugify








# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=200)
    logo = models.ImageField(null=True, blank=True, upload_to="headshots/")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)
    description = models.TextField(default='description', blank = True, null = True)
    slug = models.SlugField(primary_key=True, editable=False, max_length=200, null = False)
    popular = models.BooleanField(null=True, blank=True)
    email = models.CharField(null=True, blank=True, max_length=500)
    
    class Meta:
        verbose_name_plural = "Categories"
    

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('dash:category_detail', kwargs={'slug': self.slug})

    def _get_unique_slug(self):
        slug = slugify(self.category)
        unique_slug = slug
        num = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    
class Post(models.Model):     
    coursecategory = models.ForeignKey(
        Category,
        on_delete=models.CASCADE, blank = True, null = True)

    coursename = models.CharField(max_length=200)
    amount = models.CharField(max_length=10)
    content = RichTextField(default = 'content', blank = True, null = True)
    img = models.ImageField(null=True, blank=True, upload_to="headshots/")
    view_count = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    popular = models.BooleanField(null=True, blank=True)
    venue_1 = models.CharField(max_length=200, blank=True, null=True)
    venue_2 = models.CharField(max_length=200, blank=True, null=True)
    venue_3 = models.CharField(max_length=200, blank=True, null=True)
    venue_4 = models.CharField(max_length=200, blank=True, null=True)
    date_1 = models.DateField(null=True, blank=True)
    date_2 = models.DateField(null=True, blank=True)
    date_3 = models.DateField(null=True, blank=True)
    date_4 = models.DateField(null=True, blank=True) 
    date_5 = models.DateField(null=True, blank=True)
    date_6 = models.DateField(null=True, blank=True)
    date_7 = models.DateField(null=True, blank=True)
    date_8 = models.DateField(null=True, blank=True)  
    slug = models.SlugField(null=True, blank=True) 
    email = models.CharField(null=True, blank=True, max_length=500)
    banner = models.ImageField(null=True, blank=True, upload_to="headshots/")
    class Meta:
        verbose_name_plural = "Posts"

    def __iter__(self):

            return iter ( 
                          self.coursename,)


    def __str__(self):
        return self.coursename

    def get_absolute_url(self):
        return reverse('gov:course_detail', kwargs={'slug': self.slug})
    
    
    

class event(models.Model):
    coursename = models.CharField(max_length=250, null=True, blank=True)
    venue = models.CharField(max_length=150, null=True, blank=True )
    image = models.ImageField(null =True, blank=True, upload_to="slide/")
    description = RichTextField(default = 'content', blank = True, null = True)
    slug = models.SlugField(primary_key=True, editable=False, max_length=200, null = False)
    def __str__(self):
        return self.coursename
    def _get_unique_slug(self):
        slug = slugify(self.coursename)
        unique_slug = slug
        num = 1
        while event.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)



class Gallery(models.Model):
    name = models.CharField(max_length=20)
    pic= models.ImageField(null=True, blank=True, upload_to="headshots/")

class contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField( max_length=254)
    subject = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField(null=False, blank= False ) 
   
