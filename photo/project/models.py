from django.db import models

# Create your models here.
class Image(models.Model):
  title = models.CharField(max_length=100)
  image = models.ImageField(upload_to="./images")
  description = models.CharField(max_length=1000, blank=True, null=True)
  lower_title = models.CharField(max_length=1000, blank=True,null=True)
  lower_description = models.CharField(max_length=1000,blank=True,null=True)
