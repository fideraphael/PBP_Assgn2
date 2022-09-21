from django.db import models

class WatchListItem(models.Model):
    watched = models.TextField()
    title = models.TextField()
    rating = models.FloatField()
    release_date = models.DateField()
    review = models.CharField(max_length=255)

    # item_price = models.BigIntegerField()
    # item_stock = models.IntegerField()
    # description = models.TextField()
    # rating = models.IntegerField()
    # item_url = models.URLField()
