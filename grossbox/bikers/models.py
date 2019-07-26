from __future__ import unicode_literals
from django.db import models
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from datetime import datetime    
from django.contrib.auth.models import UserManager



# Create your models here.
CATEGORIES= (
    ('bicycle', 'Bicycle'),
    ('motor bike', 'Motor Bike'),    
)


class Biker(User):
    date_of_birth = models.DateTimeField(default=datetime.now, blank=True)
    id_number = models.IntegerField()
    residence = models.CharField(max_length = 80)
    mobile_number = models.IntegerField()
    vehiecle = models.CharField(choices = CATEGORIES,max_length = 20)
    area_of_business = models.PointField(srid=4326)
    objects = UserManager()

    def __str__(self):
        return '{}'.format(self.username)
    class Meta:
        verbose_name_plural = "Bikers" 