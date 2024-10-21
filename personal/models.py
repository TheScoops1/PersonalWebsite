from django.db import models

# Create your models here.

class Create_account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date_created = models.DateField("date created")
    last_login = models.DateTimeField('last login')
