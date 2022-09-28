from django.db import models

class WatchListItem(models.Model):
    watched = models.TextField()
    title = models.TextField()
    rating = models.FloatField()
    release_date = models.DateField()
    review = models.CharField(max_length=255)

