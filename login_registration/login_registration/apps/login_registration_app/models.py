from __future__ import unicode_literals
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import bcrypt

class UserManager(models.Manager):
    def validate_user(self, postData):
        errors = {} 

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name can not be less than 2 characters."

        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name can not be less than 2 characters."

        if len(postData['email']) < 1:
            errors['email'] = "Email cant be less than 1 character."

        if len(postData['password']) < 8:
            errors['password'] = "password cant be less than 8 characters."

        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "passwords do not match please reconfirm."
            
        try:
            validate_email(postData['email'])
        except ValidationError:
            errors['email'] = "This is not a valid email."
        else:
            if User.objects.filter(email=postData['email']):
                errors['email'] = "This user already exists."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

