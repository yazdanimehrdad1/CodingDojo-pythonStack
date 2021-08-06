from django.db import models
from datetime import datetime

# Create your models here.

class TVShowManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['title'])<2:
            errors['title'] = "Tile must be at least 3 characters"
        if len(postData['network'])<3:
            errors["network"] = "Network must be at least 3 characters"
        if  postData['description'] !='' and len(postData['description']) < 10:
            errors["description"] = "Description must be at least 10 characters "
        
        if  datetime.strptime(postData['release_date'],'%Y-%m-%d') > datetime.now():
            errors["releae_date"] = "date should be before today"
        
        return errors



class TVSHOW(models.Model):
    title = models.CharField(max_length=255)
    network   = models.CharField(max_length=45)
    release_date= models.DateTimeField(null=True)
    description = models.CharField(max_length=255, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now_add=True , null=True)
    objects = TVShowManager()




