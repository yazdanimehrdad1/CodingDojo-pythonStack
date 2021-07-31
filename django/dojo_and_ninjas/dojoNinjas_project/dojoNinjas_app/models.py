from django.db import models

# Create your models here.


class Dojo(models.Model):

    def __repr__(self):
        return f"<dojo object: {self.id} - {self.name} -{self.city} - {self.state}>"

    name = models.CharField(max_length=255)
    city =models.CharField(max_length=255)
    state= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)







