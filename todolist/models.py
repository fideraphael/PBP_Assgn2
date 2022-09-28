import datetime
from django.db import models
from django.conf import settings

class Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    date = models.DateField('',default=datetime.date.today)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

# Create your models here.
