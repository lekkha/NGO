from django.db import models

# Create your models here.

class Contact(models.Model):
    firstname = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122)
    email = models.EmailField()
    occupation = models.CharField(max_length=122)
    areacode = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    age = models.CharField()
    dob = models.DateField()
    address = models.TextField()
    address2 = models.TextField(blank=True, null=True)
    message = models.TextField()
    upload = models.FileField(upload_to='uploads/', blank=True, null=True)


