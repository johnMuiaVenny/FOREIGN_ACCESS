from django.db import models

# Create your models here.

class SINGER(models.Model):
    S_Name = models.CharField(max_length=255)
    S_Gender = models.CharField(max_length=255)
    S_Age = models.IntegerField()

    def __str__(self):
        return self.S_Name



class SONG(models.Model):
    Song_By = models.ForeignKey(SINGER, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)

    def __str__(self):
        return self.Title