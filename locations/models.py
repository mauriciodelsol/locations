from django.db import models

class Location(models.Model):
    houmer_id = models.BigIntegerField(blank=False)
    lat = models.DecimalField(max_digits=12, decimal_places=10)
    lon = models.DecimalField(max_digits=12, decimal_places=10)
    speed = models.IntegerField(blank=False, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
