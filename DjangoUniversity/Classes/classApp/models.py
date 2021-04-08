from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class djangoClass(models.Model):
    title = models.CharField(max_length=120)
    courseNumber = models.IntegerField()
    instructorName = models.CharField(max_length=50)
    duration = models.DecimalField(max_digits=1000, decimal_places=2)
