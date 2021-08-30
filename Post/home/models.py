from django.db import models
from django.contrib.auth.models import Group

new_group, created = Group.objects.get_or_create(name ='Graphic Design')
new_group1, created = Group.objects.get_or_create(name ='Finance')

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length = 40)
    company = models.CharField(max_length = 80)
    address = models.CharField(max_length = 40)
    validthrough = models.DateField(max_length = 20,null=True)
    datePosted = models.DateField(max_length=20,null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class intresting_url(models.Model):
    url = models.URLField(max_length=200)

class unintresting_url(models.Model):
    url = models.URLField(max_length = 200)
