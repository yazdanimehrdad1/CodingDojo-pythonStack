from django.db import models

# Create your models here.


class UserManager(models.Manager):
    def validator(self, postData):
        errors={}

        if len(postData['first_name'])<3:
            errors['first_name']= "first_name must be greater than 3 letters"

        if len(postData['last_name'])<3:
            errors['last_name']= "last_name must be greater than 3 letters"

        if len(postData['email'])<3:
            errors['email']= "email must be greater than 5 letters"
        return errors
    

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password=models.CharField(max_length=20)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    objects = UserManager()
