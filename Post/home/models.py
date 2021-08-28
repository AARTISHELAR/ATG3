from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length = 40)
    company = models.CharField(max_length = 80)
    address = models.CharField(max_length = 40)
    validthrough = models.DateField(max_length = 20,null=True)
    datePosted = models.DateField(max_length=20,null=True)

class intresting_url(models.Model):
    url = models.URLField(max_length=200)

class unintresting_url(models.Model):
    url = models.URLField(max_length = 200)
