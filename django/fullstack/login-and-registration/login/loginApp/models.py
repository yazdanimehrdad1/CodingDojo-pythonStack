from django.contrib.messages.api import error
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.


class UserManager(models.Manager):
    def validator(self, postData):
        errors={}

        if len(postData['first_name'])<2:
            errors['first_name']= "first_name must be greater than 2 letters"

        if len(postData['last_name'])<2:
            errors['last_name']= "last_name must be greater than 2 letters"

        if len(postData['email'])<3:
            errors['email']= "email must be greater than 5 letters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"
        if len(postData['password'])<6:
            errors['password'] ="password must be atleast 6 characters"

        if postData['password'] != postData['confirm_password']:
            errors['password'] = "Passwords do not match"
        return errors
    
    def register(self, postData):
        pw = bcrypt.hashpw(postData['password'].encode() , bcrypt.gensalt()).decode()
        return self.create(
            first_name = postData['first_name'],
            last_name = postData['last_name'],
            email = postData['email'],
            password = pw
        )

    def authenticate(self, email, password):
        users = self.filter(email = email)
        if not users:
            return False
        user = users[0]
        return bcrypt.checkpw(password.encode() , user.password.encode())
    

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password=models.CharField(max_length=20)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    objects = UserManager()
