from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(default='')

    def __str__(self):
        return self.name


class Person(models.Model):
    Pname = models.CharField(max_length=250)
    Pimg = models.ImageField(upload_to='person')
    Pdesc = models.TextField()
