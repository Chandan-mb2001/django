

# accounts/models.py
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

class CustomUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def set_password(self, raw_password):
        """Hash the password before saving."""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Check if the given raw password matches the stored hash."""
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username
