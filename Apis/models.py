from django.db import models
# from django.contrib.auth.models import AbstractUser
# Create your models here.

subscription_status = (
    ("active","active"),
    ("inactive","inactive")
)

class Subscriber(models.Model):
    first_name = models.CharField(max_length=250,)
    subscription_status = models.CharField(max_length=50, choices=subscription_status, default="active")
    email = models.EmailField(unique=True)
    
    def __str__(self):
        if self.email is not None and self.first_name is not None:
            return str(self.email) + self.first_name
        elif self.email is not None:
            return self.email
        elif  self.first_name is not None:
            return self.first_name
