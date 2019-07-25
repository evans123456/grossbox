from django.conf.urls import include,url
from . import views

app_name="accounts"


urlpatterns = [
	url(r'^$', views.index, name = 'home'),
    url(r'^register/$', views.register, name = 'register'),


]