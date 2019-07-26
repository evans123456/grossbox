from django.contrib import admin
from . import models
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class BikersAdmin(LeafletGeoAdmin):
	#pass
	list_display =('date_of_birth','id_number','residence','mobile_number','vehiecle','area_of_business')


admin.site.register(models.Biker, BikersAdmin)