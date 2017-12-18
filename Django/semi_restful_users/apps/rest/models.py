from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    def validate(self, data, action):
        # obtain form values
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']

        # define regular expressions and error flag
        name_regex = re.compile(r'^[a-zA-Z]+$')
        email_regex = re.compile(
            r'^[a-zA-Z0-9.!#$%&\u2019*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$')
        valid = True
        messages = []
        
        # make sure there are no blank fields
        for i in data:
            if len(data[i]) == 0:
                messages.append('Error: All fields are required.')
                valid = False
                break
        
        # first and last name may only contain letters
        if len(first_name) < 2 or len(last_name) < 2:
            messages.append('Error: First and last name must contain at least two characters.')
            valid = False
        elif not name_regex.match(first_name) or not name_regex.match(last_name):
            messages.append('Error: First and last name may not contain numbers or special characters.')
            valid = False

        # email format should be valid
        if len(email) > 0 and not email_regex.match(email):
            messages.append('Error: Invalid email format.')
            valid = False

        # email should not already exist
        if action == 'create':
            count = User.objects.filter(email=email).count()
            if count > 0:
                messages.append('Error: A user has already registered with that email.')
                valid = False
        
        # take action if valid, return error messages otherwise
        if valid:
            if action == 'create':
                user = User.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
            elif action == 'update':
                user = User.objects.get(id=data['user_id'])
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.save()
            return (True, user)
        else:
            return (False, messages)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
