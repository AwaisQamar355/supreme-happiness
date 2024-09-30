from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=155)
    fathername = models.CharField(max_length=155)
    studentclass = models.CharField(max_length=155)
    teachername = models.CharField(max_length=155)
    cnic = models.CharField(max_length=122)
    contact = models.CharField(max_length=155)

    def __str__(self):
        return self.name


