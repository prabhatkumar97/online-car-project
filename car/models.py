from django.db import models
from django.contrib.auth.models import User


class Categary(models.Model):
    brand=models.CharField(max_length=100,null=True)
    image = models.FileField(null=True)
    def __str__(self):
        return self.brand
class Add_Car(models.Model):
    brand=models.ForeignKey(Categary,on_delete=models.CASCADE, null=True)
    carname=models.CharField(max_length=100,null=True)
    img1 = models.FileField(null=True)
    img2 = models.FileField(null=True)
    img3 = models.FileField(null=True)
    img4 = models.FileField(null=True)
    cartype=models.CharField(max_length=100,null=True)
    bodycover=models.CharField(max_length=100,null=True)
    carmodel=models.CharField(max_length=100,null=True)
    bodytype=models.CharField(max_length=100,null=True)
    carprice=models.CharField(max_length=100,null=True)
    carnumber=models.CharField(max_length=100,null=True)
    carlength=models.IntegerField(null=True)
    carwidth=models.IntegerField(null=True)
    carheight=models.IntegerField(null=True)
    seatingcapacity=models.IntegerField(null=True)
    fueltype=models.CharField(max_length=100,null=True)
    displacement=models.CharField(max_length=100,null=True)
    maxpower=models.CharField(max_length=100,null=True)
    maxtorque=models.CharField(max_length=100,null=True)
    milage=models.CharField(max_length=100,null=True)
    transmissiontype=models.CharField(max_length=100,null=True)
    noofgear=models.CharField(max_length=100,null=True)
    aircondition=models.CharField(max_length=100,null=True)
    carpowerwindow=models.CharField(max_length=100,null=True)
    carcenterlocking=models.CharField(max_length=100,null=True)
    carabs=models.CharField(max_length=100,null=True)
    airbags=models.CharField(max_length=100,null=True)
    frontype=models.CharField(max_length=100,null=True)
    reartype=models.CharField(max_length=100,null=True)
    cardescription=models.CharField(max_length=100,null=True)
    fuelcapacity=models.CharField(max_length=100,null=True)
    bootspace=models.CharField(max_length=100,null=True)
    foglamps=models.CharField(max_length=100,null=True)
    enginedisplay=models.CharField(max_length=100,null=True)
    centrallocking=models.CharField(max_length=100,null=True)
    lastupdationdate=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.carname
class Customer(models.Model):
    Name=models.ForeignKey(Add_Car,on_delete=models.CASCADE, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    msg=models.CharField(max_length=100,null=True)
    contact=models.CharField(max_length=100,null=True)
    enquery=models.CharField(max_length=100,null=True)
    enquery_date=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True)
    remark=models.CharField(max_length=100,null=True)
    remark_date=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.user.username

class About(models.Model):
    title=models.CharField(max_length=100,null=True)
    des=models.CharField(max_length=100,null=True)
    img1 = models.FileField(null=True)
    img2 = models.FileField(null=True)
    def __str__(self):
        return self.title
class Contact(models.Model):
    contact=models.CharField(max_length=100,null=True)
    office_time=models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.contact
