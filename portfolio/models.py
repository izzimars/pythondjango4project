from distutils.command.upload import upload
from django.db import models
from django.forms import CharField
# from tables import Description

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="portfolio/images")
    url = models.URLField(blank=True)


    def __str__(self):
        return self.title

