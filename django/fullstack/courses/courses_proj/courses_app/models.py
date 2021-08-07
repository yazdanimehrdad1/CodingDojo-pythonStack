from django.db import models

# Create your models here.


class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors={}

        if len(postData["name"]) <5:
            errors["name"] = "Course name must be greater than "
        if len(postData["description"])<15:
            errors["description"] = "Desceiption must be at least 15 characters"
        return errors

class Course(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    date= models.DateField(auto_now_add=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    objects = CourseManager()



        