from django.contrib import admin
from . import models
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class CustomerAdmin(LeafletGeoAdmin):
	#pass
	list_display =('date_of_birth','id_number','residence','mobile_number','home')


admin.site.register(models.Customer, CustomerAdmin)