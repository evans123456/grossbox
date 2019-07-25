from django.contrib import admin
from . import models
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class BusinessAdmin(LeafletGeoAdmin):
	#pass
	list_display =('business_name','mobile_number','location')


admin.site.register(models.Business, BusinessAdmin)
admin.site.register(models.Foodbusiness)
admin.site.register(models.Laborbusiness)
admin.site.register(models.AvailableFoods)
admin.site.register(models.AvailableServices)



