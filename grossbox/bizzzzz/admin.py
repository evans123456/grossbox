from django.contrib import admin
from .models import Business
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class BusinessAdmin(LeafletGeoAdmin):
	#pass
	list_display =('business_name','mobile_number','location')





admin.site.register(Business, BusinessAdmin)
