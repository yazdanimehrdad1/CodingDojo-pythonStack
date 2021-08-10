from django.db import models
from datetime import datetime
import re, bcrypt
# Create your models here.
# EMAIL_REGEX = re.compile(r'^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4}')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validator_registration(self, postData):
        errors = {}
        already_exist = User.objects.filter(email=postData['email']) #?
        if len(postData['first_name'])<2:
            errors['first_name']  = "first name must be more than 2 characters"
        if len(postData['last_name'])<2:
            errors['last_name']  = "last name must be more than 2 characters"
        if len(postData['password'])<6:
            errors['password'] = "password must be atleas 6 characters"
        elif postData['password'] != postData['confirm_password']:
            errors['password'] = "Paswords do not match"

        if len(postData['email'])<1:
            errors['email'] = "email cannot be blank"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"
        elif already_exist:
            errors['email'] = "email already exist"
        return errors

    def validator_login(self, postData):
        errors={}
        check_user_exist = User.objects.filter(email = postData['email'])
        if not check_user_exist:
            errors['login_email'] = "You are not registered"
        else:
            if not bcrypt.checkpw( postData['password'].encode() , check_user_exist[0].password.encode() ):
                errors['login_email'] = "Wrong password"
        return errors



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password=models.CharField(max_length=20)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    #users_books= list of books created by this User
    #favorited_books = list of books which this user liked
    objects = UserManager()



class BookManager(models.Manager):
    def validator_book(self, postData):
        errors={}
        if len(postData['title'])<1:
            errors['title'] = "Titles can not be blank"
        if len(postData['description'])<5:
            errors['description'] = "Description must be atleast 5 characters"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    #one user that created a book
    created_by = models.ForeignKey(User, related_name="users_books", on_delete=models.CASCADE)
    #list users who liked a book
    favorited_by= models.ManyToManyField(User, related_name="favorited_books")
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    objects = BookManager()


