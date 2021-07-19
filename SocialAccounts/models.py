from django.db import models

# Create your models here.

class SOCIALaCCOUNTS(models.Model):
    Facebook = models.CharField(max_length=200, blank=True)
    Twitter = models.CharField(max_length=200, blank=True)
    Instagram = models.CharField(max_length=200, blank=True)
    YouTube = models.CharField(max_length=200, blank=True)
    LinkedIn = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.Facebook