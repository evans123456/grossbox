from django.conf.urls import include,url
from . import views

app_name="business"


urlpatterns = [
	url(r'^$', views.index, name = 'home'),
	# url(r'^county_data/$', views.county_datasets, name = 'county'),
	# url(r'^incidence_data/$', views.point_datasets, name = 'incidences'),#will change this later

]