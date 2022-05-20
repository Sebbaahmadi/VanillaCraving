from distutils.command.upload import upload
from operator import truediv
from os import link
from pickle import NONE
from turtle import title
from django.db import models
# Create your models here.
class ContactForm(models.Model):
 text=models.TextField()
 mail=models.EmailField()
 name=models.CharField(max_length=200, null=True)

