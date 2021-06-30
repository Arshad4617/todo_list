from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=5000)
    added_date = models.DateField()
