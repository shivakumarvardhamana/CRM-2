import email
from secrets import choice
from sre_constants import CATEGORY
from sre_parse import CATEGORIES
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class customer(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=250,null=True)
    phone=models.CharField(max_length=250,null=True)
    email=models.CharField(max_length=250,null=True)
    profile_pic=models.ImageField(default="img20220201_11465869.jpg",null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):

        return self.name


class Tag(models.Model):

    name=models.CharField(max_length=200,null=True)

    def __str__(self):

        return self.name


class product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor'),
    )

   

    name= models.CharField(max_length=200, null= True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200, null=True,choices=CATEGORY)
    description=models.CharField(max_length=200,null=True,blank=True)
    date_created=models.DateField(auto_now_add= True,null=True)
    tags=models.ManyToManyField(Tag)
    def __str__(self):

        return self.name

class order(models.Model):

    STATUS=(
        ('pending','pending'),
        ('Out of delivery','Out of delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey(customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(product,null=True,on_delete=models.SET_NULL)

    date_created=models.DateField(auto_now_add=True,null=True,blank=True)
    status=models.CharField(max_length=200,null=True,choices=STATUS,blank=True)
    note=models.CharField(max_length=1000,null=True)

    def __str__(self):

        return self.product.name