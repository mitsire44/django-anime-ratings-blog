from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='blog/images/', blank=True)
    title = models.CharField(max_length=75)
    desc = models.TextField(max_length=10000)
    date = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return self.title
