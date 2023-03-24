from django.db import models


class Buying(models.Model):
    estate_name = models.CharField(max_length=50, null=False, blank=True)
    owners_name = models.CharField(max_length=50, null=False, blank=True)
    units = models.IntegerField(null=False, blank=True)


def __str__(self):
    return self.estate_name
