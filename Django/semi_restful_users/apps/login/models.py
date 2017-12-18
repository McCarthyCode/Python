from __future__ import unicode_literals
from django.db import models
import re, bcrypt

class UserManager(models.Manager):
    def validate(self, data, action):
        # obtain form values
        email = data['email']
        password = data['password']
        if action == 'register':
            first_name = data['first_name']
            last_name = data['last_name']
            confirm_password = data['confirm_password']

        # define regular expressions and error flag
        name_regex = re.compile(r'^[a-zA-Z]+$')
        email_regex = re.compile(
            r'^[a-zA-Z0-9.!#$%&\u2019*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$')
        valid = True
        password_regex = re.compile(r'^(?=.*[A-Z])(?=.*\d).{8,}$')
        messages = []

        # make sure there are no blank fields
        for i in data:
            if len(data[i]) == 0:
                messages.append('Error: All fields are required.')
                valid = False
                break

        # first and last name may only contain letters
        if action == 'register':
            if len(first_name) < 2 or len(last_name) < 2:
                messages.append(
                    'Error: First and last name must contain at least two characters.')
                valid = False
            elif not name_regex.match(first_name) or not name_regex.match(last_name):
                messages.append(
                    'Error: First and last name may not contain numbers or special characters.')
                valid = False

        # email format should be valid
        if len(email) > 0 and not email_regex.match(email):
            messages.append('Error: Invalid email format.')
            valid = False

        # password must be of at least medium strength
        if action == 'register':
            if not password_regex.match(password):
                message = 'Error: Password must be at least 8 characters in length '
                message += 'containing at least 1 uppercase letter, at least 1 number, and no spaces.'
                messages.append(message)
                valid = False

        # passwords should match
        if action == 'register':
            if password != confirm_password:
                messages.append('Error: Passwords do not match.')
                valid = False

        # check if email is registered
        count = User.objects.filter(email=email).count()
        if action == 'register' and count > 0:
            messages.append('Error: A user has already registered with that email.')
            valid = False
        
        # check if password matches
        if action == 'login':
            users = User.objects.filter(email=email)
            if len(users) == 0:
                messages.append('Error: No user has registered with that email.')
                valid = False
            elif not bcrypt.checkpw(password.encode(), str(users[0].password)):
                messages.append('Error: Password does not match.')
                valid = False

        # take action if valid, return error messages otherwise
        if valid:
            if action == 'register':
                hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).encode()
                user = User.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=hashed_pw
                )
            elif action == 'login':
                user = User.objects.get(email=email)
            return (True, user)
        else:
            return (False, messages)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
