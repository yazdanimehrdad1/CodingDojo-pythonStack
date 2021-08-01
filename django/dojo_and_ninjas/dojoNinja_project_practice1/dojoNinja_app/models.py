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
    #ninjas = a list of ninjas assosiated to a Dojo


class Ninja(models.Model):

    def __repr__(self):
        return f"<dojo object: {self.id} - {self.first_name} -{self.last_name} - {self.updated_at}>"
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    dojo = models.ForeignKey(Dojo, related_name= "ninjas", on_delete=models.CASCADE ,null=True)

