from django.db import models

# Create your models here.


class TVSHOW(models.Model):
    title = models.CharField(max_length=255)
    network   = models.CharField(max_length=45)
    release_date= models.DateTimeField(null=True)
    description = models.CharField(max_length=255, null=True)




