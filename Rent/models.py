from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Car(models.Model):
    model = models.CharField(max_length=120)
    color = models.CharField(max_lenght=100)
    picture = models.ImageField(upload_to='car')
    patent = models.CharField(max_length=6,min_length=6)
    restriction = models.DateField()

    def __str__(self):
        return self.patent

class Executive(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=120)
    birthday = models.DateField()
    age = models.PositiveIntegerField()
    email = models.EmailField()
    picture = models.ImageField(upload_to='picture_executive')

    rut = models.CharField(max_length=8)
    dv = models.PositiveIntegerField()

    def full_rut(self):
        return '{}-{}' . format(self.rut, self.dv)

    def __str__(self):
        return self.name
    
class Client(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=120)
    birthday = models.DateField()
    age = models.PositiveIntegerField()
    email = models.EmailField()

    rut = models.CharField(max_length=8)
    dv = models.PositiveIntegerField()

    def full_rut(self):
        return '{}-{}' . format(self.rut, self.dv)

    def __str__(self):
        return self.name
    

class Rent(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    executive = models.ForeignKey(Executive, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def _str_(self):
        return '%s - %s - %s' % (self.client.name, self.car.patent, self.executive.name)