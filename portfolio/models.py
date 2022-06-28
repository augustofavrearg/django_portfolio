

from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.forms import URLField


# Create your models here.  
class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to='portfolio/images/')
    url = models.URLField(max_length=100, null=False, blank=True)