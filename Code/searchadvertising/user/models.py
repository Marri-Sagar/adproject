from django.db import models

# Create your models here.
class registrationmodel(models.Model):
    loginid = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    authkey = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

def __str__(self):
    return self.email

class viewdetailsmodel(models.Model):
    #category = models.CharField(max_length=100)
    property = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    price = models.IntegerField()
    #file = models.FileField(upload_to='files/pdfs/')
    rating=models.IntegerField()
    review = models.CharField(max_length=200)