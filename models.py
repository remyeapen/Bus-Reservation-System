from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BUS(models.Model):
    bus_name=models.CharField(max_length=20)
    bus_no=models.IntegerField(null=True)
    from_city=models.CharField(max_length=30)
    to_city=models.CharField(max_length=30)
    arrivaltime=models.CharField(max_length=30)
    departuretime=models.CharField(max_length=30)
    traveltime=models.CharField(max_length=30)
    distance=models.IntegerField(null=True)

class ROUTE(models.Model):
    bus=models.ForeignKey(BUS,on_delete=models.CASCADE,null=True)
    route=models.CharField(max_length=20)
    distance=models.IntegerField(null=True)
    fare=models.IntegerField(null=True)

class Register(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    dcb=models.DateField(null=True)
    gender=models.CharField(max_length=20)

class Passenger(models.Model):
    user=models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    bus=models.ForeignKey(BUS,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=20)
    age=models.IntegerField(null=True)
    gender=models.CharField(max_length=20)
    route=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    date1=models.DateField(null=True)
    fare=models.IntegerField(null=True)

class Bookticket(models.Model):
    passenger=models.ForeignKey(Passenger,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    route=models.CharField(max_length=20)
    date2=models.DateField(null=True)
    fare=models.IntegerField(null=True)

class dum(models.Model):
    fare=models.IntegerField(null=True)
    bus_name=models.CharField(max_length=20)
    date3=models.DateField(null=True)

class dum1(models.Model):
    fare=models.IntegerField(null=True)
    bus_name=models.CharField(max_length=20)
    date3=models.DateField(null=True)
