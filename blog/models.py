from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    description = models.CharField(blank=True, max_length=200)
    body = models.TextField()


    def __str__(self):
        return self.title
