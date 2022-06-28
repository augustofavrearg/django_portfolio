from distutils.command.upload import upload
from email.mime import image
from nturl2path import url2pathname

from django.db import models
from django.forms import CharField, DateField, ImageField
import datetime
from django.db.models.fields.files import ImageField

# Create your models here.
#importante usar la nomenclatura models.
class Post(models.Model):
    title =models.CharField(max_length= 100)
    descripcion = models.TextField()
    image = models.ImageField(upload_to='portfolio/static/blog/')
    fecha = models.DateField(datetime.date.today)
    