from django.db import models

class APIKEY(models.Model):
    key = models.CharField(unique=True, max_length=100,)
    length = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.key
        
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    details = models.TextField(blank=True, null=True, default="")

    def __str__(self):
        return self.name