from __future__ import unicode_literals
from django.db import models
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORIES= (
    ('vitamins', 'Fruits and Vegetables'),
    ('dairy', 'Milk and Dairy products'),
    ('cabohydrates', 'Cabohydrates, Starchy foods'),
    ('proteins','Protein'),
    ('fats and sugars','Fats and sugars'),
    
)


class Business(models.Model):
    business_name = models.CharField(max_length = 80)
    mobile_number = models.IntegerField()
    location = models.PointField(srid=4326)
    objects = GeoManager()

    def __str__(self):
        return '{}'.format(self.business_name)

    class Meta:
        verbose_name_plural = "Businesses" 

class Foodbusiness(User):
    manager_name = models.CharField(max_length = 80)
    id_number = models.IntegerField()
    residence = models.CharField(max_length = 80)
    mobile = models.IntegerField()
    biashara = models.ForeignKey('Business', on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.manager_name)
    class Meta:
        verbose_name_plural = "FoodSupply Business" 

class Laborbusiness(User):
    manager_name = models.CharField(max_length = 80)
    id_number = models.IntegerField()
    residence = models.CharField(max_length = 80)
    mobile = models.IntegerField()
    biashara = models.ForeignKey('Business', on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.manager_name)
    class Meta:
        verbose_name_plural = "Service Business" 

class AvailableFoods(models.Model):
    supplier = models.ForeignKey('Foodbusiness', on_delete=models.CASCADE)
    food = models.CharField(max_length = 80)
    category = models.CharField(choices = CATEGORIES,max_length=70)
    price_per_unit = models.IntegerField()
    def __str__(self):
        return '{} from {}'.format(self.food, self.supplier)
    class Meta:
        verbose_name_plural = "Available Foods" 
    
class AvailableServices(models.Model):
    supplier = models.ForeignKey('Laborbusiness', on_delete=models.CASCADE)
    service = models.CharField(max_length = 80)
    def __str__(self):
        return '{} from {}'.format(self.service, self.supplier)
    class Meta:
        verbose_name_plural = "Services Available" 