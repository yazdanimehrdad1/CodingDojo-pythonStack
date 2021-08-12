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
    #user_messages= list of messages created by this User
    #user_comments=list of comments created by the user
    objects = UserManager()



# class MessageManager(models.Manager):
#     def validator_book(self, postData):
#         errors={}
#         if len(postData['title'])<1:
#             errors['title'] = "Titles can not be blank"
#         if len(postData['description'])<5:
#             errors['description'] = "Description must be atleast 5 characters"
#         return errors

class Message(models.Model):
    message = models.TextField()
    #one user that created a message
    message_created_by = models.ForeignKey(User, related_name="user_messages", on_delete=models.CASCADE)
    #message_comments = list of comments that belong to a message
    user_likes = models.ManyToManyField(User, related_name='liked_posts')
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


# class CommentManager(models.Manager):
#     def validator_book(self, postData):
#         errors={}
#         if len(postData['title'])<1:
#             errors['title'] = "Titles can not be blank"
#         if len(postData['description'])<5:
#             errors['description'] = "Description must be atleast 5 characters"
#         return errors

class Comment(models.Model):
    comment = models.TextField()
    #one user that created a comment
    comment_created_by = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)
    #one message which this comment belongs to
    comment_of_message = models.ForeignKey(Message, related_name="message_comments", on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
